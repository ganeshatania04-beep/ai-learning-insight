require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./src/config/database');
const errorHandler = require('./src/middleware/errorHandler');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// Connect to Database
connectDB();

// Routes
const activityRoutes = require('./src/routes/activityRoutes');
const insightRoutes = require('./src/routes/insightRoutes');

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ 
    status: 'ok', 
    timestamp: new Date(),
    mongodb: require('mongoose').connection.readyState === 1 ? 'connected' : 'disconnected'
  });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    name: 'AI Learning Insight API',
    version: '1.0.0',
    endpoints: {
      activities: [
        'GET /api/activities/users/list',
        'GET /api/activities/:userId',
        'GET /api/activities/:userId/stats'
      ],
      insights: [
        'GET /api/insights/:userId',
        'GET /api/insights/:userId/history',
        'POST /api/insights/:userId/regenerate',
        'POST /api/insights/batch/generate'
      ]
    }
  });
});

// API Routes
app.use('/api/activities', activityRoutes);
app.use('/api/insights', insightRoutes);

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Not found' });
});

// Error handler
app.use(errorHandler);

// Start server
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log('='.repeat(50));
  console.log(`Server running on http://localhost:${PORT}`);
  console.log('='.repeat(50));
});