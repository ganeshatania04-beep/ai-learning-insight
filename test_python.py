import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend', 'model_dev'))

from predict import predict

test_activities = []

print("=" * 60)
print("AI LEARNING INSIGHT - PYTHON TEST")
print("=" * 60)
print()

print("Test 1: Empty activities")
print("-" * 40)
result = predict(test_activities)
print(f"Success: {result['success']}")
print(f"Learning Pattern: {result.get('learningPattern', 'N/A')}")
print(f"Consistency Score: {result.get('consistencyScore', 'N/A')}")
print(f"Insights: {result.get('insights', 'N/A')}")
print()

test_activities_2 = [
    {
        "date": "2024-12-01T10:00:00",
        "duration": 60,
        "timeOfDay": "morning",
        "completionStatus": True,
        "score": 85
    },
    {
        "date": "2024-12-02T14:00:00",
        "duration": 45,
        "timeOfDay": "afternoon",
        "completionStatus": True,
        "score": 90
    },
    {
        "date": "2024-12-03T10:30:00",
        "duration": 55,
        "timeOfDay": "morning",
        "completionStatus": False,
        "score": 70
    }
]

print("Test 2: With 3 activities")
print("-" * 40)
result2 = predict(test_activities_2)
print(f"Success: {result2['success']}")
print(f"Most Active Time: {result2.get('mostActiveTime', 'N/A')}")
print(f"Consistency Score: {result2.get('consistencyScore', 'N/A')}")
print(f"Learning Pattern: {result2.get('learningPattern', 'N/A')}")
print(f"Total Duration: {result2.get('totalDuration', 'N/A')} mins")
print(f"Days Active: {result2.get('daysActive', 'N/A')}")
print(f"Completion Rate: {result2.get('completionRate', 'N/A')}%")
print(f"Average Score: {result2.get('avgScore', 'N/A')}")
print(f"Insights: {result2.get('insights', 'N/A')}")
print()

print("=" * 60)
print("All tests completed successfully!")
print("=" * 60)