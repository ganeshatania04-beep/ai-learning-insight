const mongoose = require('mongoose');

const insightSchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true,
    index: true
  },
  weekStart: {
    type: Date,
    required: true,
    index: true
  },
  weekEnd: {
    type: Date,
    required: true
  },
  mostActiveTime: {
    type: String,
    enum: ['morning', 'afternoon', 'evening', 'night'],
    required: true
  },
  consistencyScore: {
    type: Number,
    min: 0,
    max: 100,
    required: true
  },
  daysActive: {
    type: Number,
    min: 0,
    max: 7,
    required: true
  },
  learningPattern: {
    type: String,
    enum: ['Consistent Learner', 'Fast Learner', 'Reflective Learner'],
    required: true
  },
  totalDuration: {
    type: Number,
    required: true,
    min: 0
  },
  totalActivities: {
    type: Number,
    required: true,
    min: 0
  },
  completionRate: {
    type: Number,
    min: 0,
    max: 100,
    required: true
  },
  avgScore: {
    type: Number,
    min: 0,
    max: 100,
    default: 0
  },
  insights: {
    type: String,
    required: true
  }
}, {
  timestamps: true
});

insightSchema.index({ userId: 1, weekStart: -1 });

module.exports = mongoose.model('Insight', insightSchema);