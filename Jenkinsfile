pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Starting the build process...'
                // Windows equivalent build commands
                bat 'npm install' // Example build command for Windows
                echo 'Build successful!'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Windows equivalent test commands
                bat 'npm test' // Example test command for Windows
                echo 'Tests passed!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Windows equivalent deploy commands
                bat 'npm run deploy' // Example deploy command for Windows
                echo 'Deployment successful!'
            }
        }
    }
}
