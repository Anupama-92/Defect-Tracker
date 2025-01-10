pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add your build commands here, e.g., 'mvn clean package' for a Maven project
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add test commands here, e.g., 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deployment steps here
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Add cleanup steps, e.g., deleting temporary files
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}