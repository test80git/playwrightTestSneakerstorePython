pipeline {
    agent any
    
    environment {
        HEADLESS = 'true'
        PYTHONUNBUFFERED = '1'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install --break-system-packages -r requirements.txt
                    playwright install chromium
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    cd $WORKSPACE
                    python3 -m pytest tests/ -v --alluredir=allure-results
                '''
            }
        }
        
        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}

