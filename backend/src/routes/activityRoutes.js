const express = require('express');
const router = express.Router();
const {
  getUserActivities,
  getUserActivityStats,
  getAllUsers
} = require('../controllers/activityController');

router.get('/users/list', getAllUsers);
router.get('/:userId', getUserActivities);
router.get('/:userId/stats', getUserActivityStats);

module.exports = router;