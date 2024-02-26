pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Starting the build process...'
                // Add build commands here
                sh 'npm install' // Example build command
                echo 'Build successful!'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here
                sh 'npm test' // Example test command
                echo 'Tests passed!'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add deploy commands here
                sh 'npm run deploy' // Example deploy command
                echo 'Deployment successful!'
            }
        }
    }
}
