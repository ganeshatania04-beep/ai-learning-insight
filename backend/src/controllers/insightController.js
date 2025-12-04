const LearningActivity = require('../models/LearningActivity');
const Insight = require('../models/Insight');
const { generateInsights } = require('../services/mlService');

const getCurrentInsights = async (req, res, next) => {
  try {
    const { userId } = req.params;

    const activities = await LearningActivity.find({ userId })
      .sort({ date: -1 })
      .limit(50);

    if (activities.length === 0) {
      return res.json({
        success: true,
        message: 'Belum ada aktivitas belajar',
        data: null
      });
    }

    const result = await generateInsights(activities);

    const insight = await Insight.create({
      userId,
      weekStart: new Date(),
      weekEnd: new Date(),
      ...result
    });

    res.json({
      success: true,
      data: insight
    });

  } catch (error) {
    next(error);
  }
};

const getInsightsHistory = async (req, res, next) => {
  try {
    const { userId } = req.params;
    const { limit = 10 } = req.query;

    const insights = await Insight.find({ userId })
      .sort({ createdAt: -1 })
      .limit(parseInt(limit));

    res.json({
      success: true,
      count: insights.length,
      data: insights
    });

  } catch (error) {
    next(error);
  }
};

const regenerateInsights = async (req, res, next) => {
  try {
    const { userId } = req.params;
    
    console.log('UserId:', userId);
    console.log('Body:', req.body);
    console.log('Activities:', req.body.activities);

    const activities = req.body.activities || [];

    if (!activities || activities.length === 0) {
      return res.status(400).json({
        success: false,
        error: 'Tidak ada aktivitas untuk diproses'
      });
    }

    const result = await generateInsights(activities);

    const insight = await Insight.create({
      userId,
      weekStart: new Date(),
      weekEnd: new Date(),
      ...result
    });

    res.json({
      success: true,
      message: 'Insights berhasil di-regenerate',
      data: insight
    });

  } catch (error) {
    next(error);
  }
};

const batchGenerateInsights = async (req, res, next) => {
  try {
    const users = await LearningActivity.distinct('userId');
    const results = [];

    for (const userId of users) {
      const activities = await LearningActivity.find({ userId })
        .sort({ date: -1 })
        .limit(50);

      if (activities.length > 0) {
        const result = await generateInsights(activities);
        
        const insight = await Insight.create({
          userId,
          weekStart: new Date(),
          weekEnd: new Date(),
          ...result
        });

        results.push(insight);
      }
    }

    res.json({
      success: true,
      message: `Generated insights for ${results.length} users`,
      data: results
    });

  } catch (error) {
    next(error);
  }
};

module.exports = {
  getCurrentInsights,
  getInsightsHistory,
  regenerateInsights,
  batchGenerateInsights
};