const http = require('http');

const BASE_URL = 'localhost';
const PORT = 5000;

const sampleActivities = [
  {
    date: '2024-12-01T10:00:00Z',
    duration: 60,
    timeOfDay: 'morning',
    courseName: 'Machine Learning',
    activityType: 'video',
    completionStatus: true,
    score: 85
  },
  {
    date: '2024-12-02T14:30:00Z',
    duration: 45,
    timeOfDay: 'afternoon',
    courseName: 'Web Development',
    activityType: 'reading',
    completionStatus: true,
    score: 90
  },
  {
    date: '2024-12-03T10:00:00Z',
    duration: 90,
    timeOfDay: 'morning',
    courseName: 'Data Science',
    activityType: 'quiz',
    completionStatus: true,
    score: 88
  }
];

function makeRequest(options, data) {
  return new Promise((resolve, reject) => {
    const req = http.request(options, (res) => {
      let body = '';
      
      res.on('data', (chunk) => {
        body += chunk;
      });
      
      res.on('end', () => {
        try {
          const result = JSON.parse(body);
          resolve({ statusCode: res.statusCode, data: result });
        } catch (error) {
          resolve({ statusCode: res.statusCode, data: body });
        }
      });
    });

    req.on('error', (error) => {
      reject(error);
    });

    req.setTimeout(5000, () => {
      req.destroy();
      reject(new Error('Request timeout after 5 seconds'));
    });

    if (data) {
      req.write(data);
    }
    req.end();
  });
}

async function checkHealth() {
  console.log('Checking server health...');
  
  try {
    const options = {
      hostname: BASE_URL,
      port: PORT,
      path: '/health',
      method: 'GET',
      timeout: 3000
    };

    const result = await makeRequest(options);
    
    if (result.statusCode === 200) {
      console.log('Server is running\n');
      return true;
    } else {
      console.log('Server responded with status:', result.statusCode);
      return false;
    }
  } catch (error) {
    console.log('\nERROR: Cannot connect to server!');
    console.log('Message:', error.message);
    console.log('\nPlease make sure:');
    console.log('1. Server is running in another terminal');
    console.log('2. Run command: npm run dev');
    console.log('3. Check if port 5000 is free\n');
    return false;
  }
}

async function testGenerateInsights() {
  console.log('Testing Generate Insights endpoint...');
  console.log('Sample activities:', sampleActivities.length, 'items\n');

const data = JSON.stringify({
  activities: sampleActivities
});

console.log('Sending data:', data.substring(0, 100) + '...');

  const options = {
    hostname: BASE_URL,
    port: PORT,
    path: '/api/insights/test_user_001/regenerate',  
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(data)
    },
    timeout: 10000
  };


  try {
    const result = await makeRequest(options, data);
    
    console.log('Status Code:', result.statusCode);
    
    if (result.statusCode === 200 && result.data.success) {
      console.log('TEST PASSED!');
      
      const insights = result.data.data;
      
      console.log('INSIGHTS GENERATED:');
      console.log('Most Active Time   :', insights.mostActiveTime);
      console.log('Consistency Score  :', insights.consistencyScore + '/100');
      console.log('Days Active        :', insights.daysActive + '/7');
      console.log('Learning Pattern   :', insights.learningPattern);
      console.log('Total Duration     :', insights.totalDuration, 'minutes');
      console.log('Total Activities   :', insights.totalActivities);
      console.log('Completion Rate    :', insights.completionRate + '%');
      console.log('Average Score      :', insights.avgScore);
      
      console.log('\nINSIGHT TEXT:');
      console.log(insights.insights);
      
      console.log('Backend is working correctly!');

      return true;
    } else {
      console.log('\nTEST FAILED!');
      console.log('Response:', JSON.stringify(result.data, null, 2));
      return false;
    }
  } catch (error) {
    console.log('\nERROR during test:');
    console.log('Message:', error.message);
    
    if (error.message.includes('timeout')) {
      console.log('\nPossible causes:');
      console.log('1. Python script taking too long');
      console.log('2. Python not installed or not in PATH');
      console.log('3. predict.py file missing in model_dev folder');
      console.log('\nCheck backend terminal for error messages.');
    }
    
    return false;
  }
}

async function runTests() {
  console.log('AI Learning Insight - Backend Test');


  const serverOk = await checkHealth();
  
  if (!serverOk) {
    console.log('Aborting tests. Please start the server first.\n');
    process.exit(1);
  }

  const testOk = await testGenerateInsights();
  
  if (testOk) {
    console.log('All tests completed successfully!\n');
    process.exit(0);
  } else {
    console.log('Some tests failed. Check the output above.\n');
    process.exit(1);
  }
}

runTests();