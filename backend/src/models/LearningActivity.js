const mongoose = require('mongoose');

const learningActivitySchema = new mongoose.Schema({
  userId: {
    type: String,
    required: true,
    index: true
  },
  date: {
    type: Date,
    required: true,
    index: true
  },
  dayOfWeek: {
    type: String,
    enum: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    required: true
  },
  timeOfDay: {
    type: String,
    enum: ['morning', 'afternoon', 'evening', 'night'],
    required: true
  },
  duration: {
    type: Number,
    required: true,
    min: 1
  },
  courseName: {
    type: String,
    required: true,
    trim: true
  },
  activityType: {
    type: String,
    enum: ['video', 'reading', 'quiz', 'assignment', 'discussion'],
    required: true
  },
  completionStatus: {
    type: Boolean,
    default: false
  },
  score: {
    type: Number,
    min: 0,
    max: 100,
    default: null
  }
}, {
  timestamps: true
});

learningActivitySchema.index({ userId: 1, date: -1 });

module.exports = mongoose.model('LearningActivity', learningActivitySchema);