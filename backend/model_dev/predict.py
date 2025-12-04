import sys
import json
import numpy as np

def calculate_most_active_time(activities):
    time_counts = {'morning': 0, 'afternoon': 0, 'evening': 0, 'night': 0}
    for a in activities:
        tod = a.get('timeOfDay', 'morning')
        time_counts[tod] = time_counts.get(tod, 0) + 1
    return max(time_counts, key=time_counts.get)

def calculate_consistency_score(features):
    unique_days = features['unique_days']
    total_days = 7
    days_score = (unique_days / total_days) * 100
    completion_bonus = features['completion_rate'] * 10
    
    if features['avg_duration'] > 0:
        cv = features['std_duration'] / features['avg_duration']
        consistency_penalty = min(cv * 5, 10)
    else:
        consistency_penalty = 0
    
    score = days_score + completion_bonus - consistency_penalty
    score = max(0, min(100, score))
    return round(score, 2)

def determine_learning_pattern(features):
    unique_days = features['unique_days']
    avg_duration = features['avg_duration']
    completion_rate = features['completion_rate']
    avg_score = features['avg_score']
    
    if unique_days >= 5 and completion_rate >= 0.7:
        return 'Consistent Learner'
    elif avg_duration < 45 and completion_rate >= 0.8 and avg_score >= 75:
        return 'Fast Learner'
    else:
        return 'Reflective Learner'

def generate_insight_text(result):
    pattern = result['learningPattern']
    active_time = result['mostActiveTime']
    consistency = result['consistencyScore']
    days_active = result['daysActive']
    
    time_id = {
        'morning': 'pagi',
        'afternoon': 'siang', 
        'evening': 'sore',
        'night': 'malam'
    }
    
    insight = f"Minggu ini kamu belajar selama {days_active} dari 7 hari. "
    insight += f"Waktu paling aktif kamu adalah {time_id.get(active_time, active_time)}. "
    
    if consistency >= 80:
        insight += "Tingkat konsistensimu sangat tinggi! "
    elif consistency >= 60:
        insight += "Tingkat konsistensimu baik. "
    elif consistency >= 40:
        insight += "Tingkat konsistensimu cukup. "
    else:
        insight += "Tingkatkan konsistensi belajarmu. "
    
    if pattern == 'Consistent Learner':
        insight += "Kamu adalah Consistent Learner! "
    elif pattern == 'Fast Learner':
        insight += "Kamu adalah Fast Learner! "
    else:
        insight += "Kamu adalah Reflective Learner! "
    
    return insight

def prepare_features(activities):
    if not activities:
        return None
    
    durations = [a['duration'] for a in activities]
    features = {
        'total_duration': sum(durations),
        'avg_duration': np.mean(durations),
        'std_duration': np.std(durations) if len(durations) > 1 else 0,
        'total_activities': len(activities),
        'unique_days': len(set(a['date'].split('T')[0] for a in activities))
    }
    
    completed = [a for a in activities if a.get('completionStatus', False)]
    features['completion_rate'] = len(completed) / len(activities) if activities else 0
    
    scores = [a.get('score', 0) for a in activities if a.get('score') is not None]
    features['avg_score'] = np.mean(scores) if scores else 0
    
    return features

def predict(activities):
    try:
        if not activities:
            return {
                'success': True,
                'mostActiveTime': 'morning',
                'consistencyScore': 0,
                'daysActive': 0,
                'learningPattern': 'Reflective Learner',
                'totalDuration': 0,
                'totalActivities': 0,
                'completionRate': 0,
                'avgScore': 0,
                'insights': 'Belum ada data aktivitas belajar.'
            }
        
        features = prepare_features(activities)
        if not features:
            raise ValueError("Cannot prepare features")
        
        most_active_time = calculate_most_active_time(activities)
        consistency_score = calculate_consistency_score(features)
        learning_pattern = determine_learning_pattern(features)
        
        result = {
            'success': True,
            'mostActiveTime': most_active_time,
            'consistencyScore': consistency_score,
            'daysActive': features['unique_days'],
            'learningPattern': learning_pattern,
            'totalDuration': int(features['total_duration']),
            'totalActivities': features['total_activities'],
            'completionRate': round(features['completion_rate'] * 100, 2),
            'avgScore': round(features['avg_score'], 2)
        }
        
        result['insights'] = generate_insight_text(result)
        return result
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("No input")
        
        input_data = json.loads(sys.argv[1])
        activities = input_data.get('activities', [])
        result = predict(activities)
        print(json.dumps(result))
        
    except Exception as e:
        error_result = {
            'success': False,
            'error': str(e)
        }
        print(json.dumps(error_result))
        sys.exit(1)

if __name__ == '__main__':
    main()