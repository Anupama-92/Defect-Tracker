pipeline {
    agent any
    environment {
        VENV_DIR = '.venv' // Virtual environment
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Anupama-92/Defect-Tracker.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh '$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '$VENV_DIR/bin/python -m pytest --html=report.html --self-contained-html'
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML([allowMissing: false,
                             alwaysLinkToLastBuild: true,
                             keepAll: true,
                             reportDir: '.',
                             reportFiles: 'report.html',
                             reportName: 'Selenium Test Report'])
            }
        }
    }
    post {
        always {
            cleanWs() // Clean workspace after the build
        }
    }
}
