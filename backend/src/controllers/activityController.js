const LearningActivity = require('../models/LearningActivity');

const getUserActivities = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const { startDate, endDate, limit = 100 } = req.query;

    let query = { userId };

    if (startDate || endDate) {
      query.date = {};
      if (startDate) query.date.$gte = new Date(startDate);
      if (endDate) query.date.$lte = new Date(endDate);
    }

    const activities = await LearningActivity.find(query)
      .sort({ date: -1 })
      .limit(parseInt(limit));

    res.json({
      success: true,
      count: activities.length,
      data: activities
    });

  } catch (error) {
    next(error);
  }
};

const getUserActivityStats = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const { startDate, endDate } = req.query;

    let matchQuery = { userId };

    if (startDate || endDate) {
      matchQuery.date = {};
      if (startDate) matchQuery.date.$gte = new Date(startDate);
      if (endDate) matchQuery.date.$lte = new Date(endDate);
    }

    const stats = await LearningActivity.aggregate([
      { $match: matchQuery },
      {
        $group: {
          _id: null,
          totalActivities: { $sum: 1 },
          totalDuration: { $sum: '$duration' },
          avgDuration: { $avg: '$duration' },
          completedActivities: { $sum: { $cond: ['$completionStatus', 1, 0] } },
          avgScore: { $avg: { $cond: [{ $ne: ['$score', null] }, '$score', null] } }
        }
      }
    ]);

    const result = stats[0] || {
      totalActivities: 0,
      totalDuration: 0,
      avgDuration: 0,
      completedActivities: 0,
      avgScore: 0
    };

    result.completionRate = result.totalActivities > 0
      ? ((result.completedActivities / result.totalActivities) * 100).toFixed(2)
      : 0;

    result.avgDuration = Math.round(result.avgDuration || 0);
    result.avgScore = Math.round(result.avgScore || 0);

    res.json({
      success: true,
      data: result
    });

  } catch (error) {
    next(error);
  }
};

const getAllUsers = async (req, res, next) => {
  try {
    const users = await LearningActivity.distinct('userId');

    res.json({
      success: true,
      count: users.length,
      data: users
    });

  } catch (error) {
    next(error);
  }
};

module.exports = {
  getUserActivities,
  getUserActivityStats,
  getAllUsers
};