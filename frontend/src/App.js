import React, { useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  TextField,
  Button,
  Paper,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
  Box,
} from '@mui/material';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/chat', { query });
      setResponse(res.data.response);
      setHistory([
        ...history,
        {
          query,
          response: res.data.response,
          timestamp: new Date().toLocaleString(),
        },
      ]);
      setQuery('');
    } catch (error) {
      console.error('Error:', error);
      setResponse('Failed to fetch response');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      {/* Header */}
      <Typography variant="h3" component="h1" align="center" gutterBottom>
        Supplier Product Chatbot
      </Typography>

      {/* Query Input Area */}
      <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
        <TextField
          fullWidth
          multiline
          rows={4}
          variant="outlined"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about products or suppliers..."
          disabled={loading}
        />
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : 'Ask'}
          </Button>
        </Box>
      </Paper>

      {/* Response Display */}
      {response && (
        <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
          <Typography variant="h5" component="h2" gutterBottom>
            Response:
          </Typography>
          <Typography variant="body1" component="pre" sx={{ whiteSpace: 'pre-wrap' }}>
            {response}
          </Typography>
        </Paper>
      )}

      {/* Query History */}
      <Paper elevation={3} sx={{ p: 3 }}>
        <Typography variant="h5" component="h2" gutterBottom>
          Query History
        </Typography>
        <List>
          {history.slice().reverse().map((item, index) => (
            <ListItem key={index} sx={{ mb: 2, bgcolor: 'background.paper' }}>
              <ListItemText
                primary={
                  <>
                    <Typography variant="body1" component="span" sx={{ fontWeight: 'bold' }}>
                      Query:
                    </Typography>{' '}
                    {item.query}
                  </>
                }
                secondary={
                  <>
                    <Typography variant="body2" component="span" sx={{ fontWeight: 'bold' }}>
                      Response:
                    </Typography>{' '}
                    {item.response}
                    <br />
                    <Typography variant="caption" component="span">
                      {item.timestamp}
                    </Typography>
                  </>
                }
              />
            </ListItem>
          ))}
        </List>
      </Paper>
    </Container>
  );
}

export default App;