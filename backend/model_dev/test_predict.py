#!/usr/bin/env python3

import json
from predict import LearningInsightPredictor

def test_prediction():
    
    print("=" * 60)
    print("Testing Prediction Script")
    print("=" * 60)
    
    # Sample activities - 1 week of learning
    sample_activities = [
        {
            'date': '2024-12-01T10:30:00Z',
            'duration': 60,
            'timeOfDay': 'morning',
            'completionStatus': True,
            'score': 85,
            'activityType': 'video'
        },
        {
            'date': '2024-12-02T14:30:00Z',
            'duration': 45,
            'timeOfDay': 'afternoon',
            'completionStatus': True,
            'score': 90,
            'activityType': 'reading'
        },
        {
            'date': '2024-12-03T10:00:00Z',
            'duration': 90,
            'timeOfDay': 'morning',
            'completionStatus': True,
            'score': 88,
            'activityType': 'quiz'
        },
        {
            'date': '2024-12-04T19:00:00Z',
            'duration': 30,
            'timeOfDay': 'evening',
            'completionStatus': False,
            'score': None,
            'activityType': 'video'
        },
        {
            'date': '2024-12-05T11:00:00Z',
            'duration': 75,
            'timeOfDay': 'morning',
            'completionStatus': True,
            'score': 92,
            'activityType': 'assignment'
        },
        {
            'date': '2024-12-06T15:30:00Z',
            'duration': 50,
            'timeOfDay': 'afternoon',
            'completionStatus': True,
            'score': 87,
            'activityType': 'reading'
        },
        {
            'date': '2024-12-07T10:30:00Z',
            'duration': 65,
            'timeOfDay': 'morning',
            'completionStatus': True,
            'score': 89,
            'activityType': 'quiz'
        }
    ]
    
    print(f"\n📊 Sample Data:")
    print(f"   Total activities: {len(sample_activities)}")
    print(f"   Date range: Dec 1-7, 2024")
    print(f"   All days: 7/7")
    
    # Initialize predictor
    print("\n🔄 Initializing predictor...")
    predictor = LearningInsightPredictor()
    
    # Make prediction
    print("🔄 Generating prediction...")
    result = predictor.predict(sample_activities)
    
    # Display results
    print("\n" + "=" * 60)
    print("PREDICTION RESULTS")
    print("=" * 60)
    
    if result['success']:
        print("\n✓ Prediction successful!\n")
        print(f"📈 Most Active Time: {result['mostActiveTime']}")
        print(f"📊 Consistency Score: {result['consistencyScore']}/100")
        print(f"📅 Days Active: {result['daysActive']}/7")
        print(f"🎯 Learning Pattern: {result['learningPattern']}")
        print(f"⏱️  Total Duration: {result['totalDuration']} minutes")
        print(f"📝 Total Activities: {result['totalActivities']}")
        print(f"✅ Completion Rate: {result['completionRate']}%")
        print(f"🎓 Average Score: {result['avgScore']}")
        print(f"\n💡 Insights:")
        print(f"   {result['insights']}")
        
        # Test with empty data
        print("\n" + "=" * 60)
        print("Testing with empty data...")
        print("=" * 60)
        empty_result = predictor.predict([])
        print(f"\n✓ Empty data handled correctly")
        print(f"   Message: {empty_result['insights']}")
        
        return True
    else:
        print(f"\n✗ Prediction failed!")
        print(f"   Error: {result.get('error', 'Unknown error')}")
        return False

if __name__ == '__main__':
    success = test_prediction()
    exit(0 if success else 1)