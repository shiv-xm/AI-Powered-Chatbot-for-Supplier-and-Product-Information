from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langgraph.graph import StateGraph, END

# Corrected Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 5000,
    "user": "root",
    "password": "*********",
    "database": "supplierproductdb"
}

# Create database connection
db_uri = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
sql_database = SQLDatabase.from_uri(db_uri)

# LLM and Language Models
llm = OllamaLLM(model="llama2")


# Define the state
class GraphState:
    query: str
    intermediate_steps: List[str]
    final_response: str


# Nodes for the workflow
def query_understanding(state: GraphState):
    """Understand the user's query intent"""
    prompt = PromptTemplate.from_template(
        "Analyze the following query and determine its intent: {query}"
    )
    chain = prompt | llm | StrOutputParser()
    intent = chain.invoke({"query": state.query})

    return {
        "intermediate_steps": state.intermediate_steps + [f"Query Intent: {intent}"]
    }


def database_retrieval(state: GraphState):
    """Retrieve relevant information from database"""
    try:
        # Use SQL Database to generate and execute query
        results = sql_database.run(state.query)
        return {
            "intermediate_steps": state.intermediate_steps + [f"Database Results: {results}"],
            "final_response": str(results)
        }
    except Exception as e:
        return {
            "intermediate_steps": state.intermediate_steps + [f"Database Error: {str(e)}"],
            "final_response": "Could not retrieve information"
        }


def response_generation(state: GraphState):
    """Generate final response using LLM"""
    prompt = PromptTemplate.from_template(
        "Based on the query intent and database results, provide a clear response: {results}"
    )
    chain = prompt | llm | StrOutputParser()
    final_response = chain.invoke({"results": state.final_response})

    return {
        "final_response": final_response
    }


# Build the graph
def build_workflow():
    graph = StateGraph(GraphState)

    graph.add_node("query_understanding", query_understanding)
    graph.add_node("database_retrieval", database_retrieval)
    graph.add_node("response_generation", response_generation)

    graph.add_edge("query_understanding", "database_retrieval")
    graph.add_edge("database_retrieval", "response_generation")
    graph.add_edge("response_generation", END)

    graph.set_entry_point("query_understanding")

    return graph.compile()


# Initialize the workflow
workflow = build_workflow()

# FastAPI App
app = FastAPI()

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.post("/chat")
async def chatbot(request: QueryRequest):
    try:
        # Run the workflow
        initial_state = {
            "query": request.query,
            "intermediate_steps": [],
            "final_response": ""
        }

        result = workflow.invoke(initial_state)

        return {"response": result['final_response']}
    except Exception as e:
        return {"response": f"Error processing query: {str(e)}"}


