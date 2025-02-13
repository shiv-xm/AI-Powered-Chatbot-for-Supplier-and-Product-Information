# AI-Powered-Chatbot-for-Supplier-and-Product-Information
<!-- README.md -->
<div style="font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px;">

  <!-- Header -->
  <h1 style="font-size: 2.5rem; font-weight: bold; color: #1a365d; text-align: center; margin-bottom: 20px;">
    AI-Powered Chatbot for Supplier and Product Information
  </h1>

  <!-- Overview -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Overview</h2>
    <p style="color: #4a5568; line-height: 1.6;">
      This project is an AI-powered chatbot designed to interact with a MySQL database containing supplier and product information. The chatbot uses natural language processing (NLP) to understand user queries, retrieves relevant data from the database, and generates responses using an open-source LLM (LLaMA 2). The backend is built with Python (FastAPI) and LangGraph, while the frontend is developed using React and styled with <strong>Material UI</strong>.
    </p>
  </div>

  <!-- Features -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Features</h2>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li><strong>Natural Language Querying:</strong> Users can ask questions like:
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>"Show me all products under brand X."</li>
          <li>"Which suppliers provide laptops?"</li>
          <li>"Give me details of product ABC."</li>
        </ul>
      </li>
      <li><strong>Database Interaction:</strong> The chatbot retrieves data from a MySQL database containing product and supplier information.</li>
      <li><strong>LLM-Powered Summarization:</strong> The chatbot uses LLaMA 2 to enhance responses with context and summarization.</li>
      <li><strong>Conversational Interface:</strong> The frontend provides a user-friendly interface for interacting with the chatbot and viewing query history.</li>
    </ul>
  </div>

  <!-- Technologies Used -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Technologies Used</h2>
    <div style="color: #4a5568; line-height: 1.6;">
      <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-bottom: 5px;">Backend</h3>
      <ul style="list-style-type: disc; padding-left: 20px;">
        <li>Python (FastAPI)</li>
        <li>LangGraph for workflow management</li>
        <li>LLaMA 2 (via OllamaLLM) for natural language processing</li>
        <li>MySQL for database management</li>
      </ul>
      <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-top: 10px; margin-bottom: 5px;">Frontend</h3>
      <ul style="list-style-type: disc; padding-left: 20px;">
        <li>React for the user interface</li>
        <li>Material-UI (MUI) for styling and pre-built components</li>
        <li>Axios for API calls</li>
      </ul>
    </div>
  </div>

  <!-- Database Schema -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Database Schema</h2>
    <p style="color: #4a5568; line-height: 1.6;">
      The database consists of two main tables:
    </p>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li><strong>Products:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li><code>ID</code> (Primary Key)</li>
          <li><code>name</code></li>
          <li><code>brand</code></li>
          <li><code>price</code></li>
          <li><code>category</code></li>
          <li><code>description</code></li>
          <li><code>supplier_id</code> (Foreign Key)</li>
        </ul>
      </li>
      <li><strong>Suppliers:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li><code>ID</code> (Primary Key)</li>
          <li><code>name</code></li>
          <li><code>contact_info</code></li>
          <li><code>product_categories_offered</code></li>
        </ul>
      </li>
    </ul>
  </div>

  <!-- Setup Instructions -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Setup Instructions</h2>
    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-bottom: 5px;">Prerequisites</h3>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li>Python 3.8+</li>
      <li>Node.js (for frontend)</li>
      <li>MySQL Server</li>
      <li>Ollama (for running LLaMA 2 locally)</li>
    </ul>
    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-top: 10px; margin-bottom: 5px;">Backend Setup</h3>
    <ol style="color: #4a5568; line-height: 1.6; list-style-type: decimal; padding-left: 20px;">
      <li>Clone the repository:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>git clone &lt;repository-url&gt;
cd backend</code>
        </pre>
      </li>
      <li>Install Python dependencies:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>pip install -r requirements.txt</code>
        </pre>
      </li>
      <li>Set up the MySQL database:
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>Create a database named <code>supplierproductdb</code>.</li>
          <li>Import the schema and sample data using the provided SQL scripts.</li>
        </ul>
      </li>
      <li>Configure the database connection in <code>main.py</code>:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>DB_CONFIG = {
  "host": "localhost",
  "port": 5000,
  "user": "root",
  "password": "********",
  "database": "supplierproductdb"
}</code>
        </pre>
      </li>
      <li>Run the FastAPI server:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>uvicorn main:app --reload</code>
        </pre>
      </li>
    </ol>
    <h3 style="font-size: 1.5rem; font-weight: bold; color: #2d3748; margin-top: 10px; margin-bottom: 5px;">Frontend Setup</h3>
    <ol style="color: #4a5568; line-height: 1.6; list-style-type: decimal; padding-left: 20px;">
      <li>Navigate to the frontend directory:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>cd frontend</code>
        </pre>
      </li>
      <li>Install Node.js dependencies:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>npm install</code>
        </pre>
      </li>
      <li>Install Material-UI:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>npm install @mui/material @emotion/react @emotion/styled @mui/icons-material</code>
        </pre>
      </li>
      <li>Run the React app:
        <pre style="background-color: #edf2f7; padding: 10px; border-radius: 6px; margin-top: 5px;">
          <code>npm start</code>
        </pre>
      </li>
      <li>Access the frontend at <code>http://localhost:3000</code>.</li>
    </ol>
  </div>

  <!-- Usage -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Usage</h2>
    <ol style="color: #4a5568; line-height: 1.6; list-style-type: decimal; padding-left: 20px;">
      <li>Enter a query in the text area (e.g., "Show me all products under brand X").</li>
      <li>Click the "Ask" button to submit the query.</li>
      <li>View the chatbot's response below the input area.</li>
      <li>Check the query history for past interactions.</li>
    </ol>
  </div>

  <!-- API Endpoints -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">API Endpoints</h2>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li><strong>POST <code>/chat</code>:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>Accepts a JSON payload with a <code>query</code> field.</li>
          <li>Returns a JSON response with the chatbot's response.</li>
        </ul>
      </li>
    </ul>
  </div>

  <!-- Example Queries -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Example Queries</h2>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li>"Show me all products under brand Apple."</li>
      <li>"Which suppliers provide laptops?"</li>
      <li>"Give me details of product ABC123."</li>
    </ul>
  </div>

  <!-- Evaluation Criteria -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Evaluation Criteria</h2>
    <ul style="color: #4a5568; line-height: 1.6; list-style-type: disc; padding-left: 20px;">
      <li><strong>Functionality:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>Completeness of chatbot interactions.</li>
          <li>Accuracy of data retrieval and filtering.</li>
        </ul>
      </li>
      <li><strong>Code Quality:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>Clean, modular, and well-documented code.</li>
        </ul>
      </li>
      <li><strong>Scalability:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>Efficient query handling and performance.</li>
        </ul>
      </li>
      <li><strong>UI/UX:</strong>
        <ul style="list-style-type: circle; padding-left: 20px;">
          <li>User-friendly design and responsiveness.</li>
        </ul>
      </li>
    </ul>
  </div>


  <!-- Contributors -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">Contributors</h2>
    <p style="color: #4a5568; line-height: 1.6;">
      - Sudhanshu Shivam
    </p>
  </div>

  <!-- License -->
  <div style="background-color: #f7fafc; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
    <h2 style="font-size: 1.875rem; font-weight: bold; color: #2d3748; margin-bottom: 10px;">License</h2>
    <p style="color: #4a5568; line-height: 1.6;">
      This project is licensed under the MIT License. See the <a href="LICENSE" style="color: #3182ce; text-decoration: underline;">LICENSE</a> file for details.
    </p>
  </div>

</div>
