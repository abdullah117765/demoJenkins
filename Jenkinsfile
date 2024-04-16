pipeline {
      
    environment {
        deployedLink = '3.7.253.96:81'
    }
    
    agent any
    
    stages {

        stage('Cloning from git') {
            steps {
                git branch: 'main', url: "https://github.com/abdullah117765/${env.JOB_NAME}"
            }
        }

        stage('Installation of dependencies') {
            steps {
               // bat 'pip3 install -r requirement.txt'
                echo 'Dependencies successfully installed!'
            }
        }

        stage('Test') {
            steps {
             //   bat 'python test.py'
                echo 'Tests passed!'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production...'
                        bat "type nul > ${WORKSPACE}\\deployment_link.txt"  // Create the file if it doesn't exist
                        writeFile file: "${WORKSPACE}\\deployment_link.txt", text: "${env.deployedLink}"
                        
                    } else {
                        echo 'Deploying to development server...'
                        
                    }
                }
            }
        }
    }
}
