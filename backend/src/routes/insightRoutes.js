const express = require('express');
const router = express.Router();
const {
  getCurrentInsights,
  getInsightsHistory,
  regenerateInsights,
  batchGenerateInsights
} = require('../controllers/insightController');

router.post('/batch/generate', batchGenerateInsights);
router.get('/:userId', getCurrentInsights);
router.get('/:userId/history', getInsightsHistory);
router.post('/:userId/regenerate', regenerateInsights);


module.exports = router;