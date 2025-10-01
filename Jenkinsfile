pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/haarthee/Sample_Webserver.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Start Flask App') {
            steps {
                sh 'source venv/bin/activate && nohup python3 app.py &'
                sh 'sleep 5'  // Wait for server to start
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest Selenium_pytest_tests/'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'pkill -f "python3 app.py" || true'
            }
        }
    }
}
