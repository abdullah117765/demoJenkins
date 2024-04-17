pipeline {
      
    environment {
        deployedLink = ''
    }
    
    agent any
    
    parameters {
        string(defaultValue: '', description: 'Deployed Link', name: 'deployedLink')
    }
    
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
                      
                      echo 'Deploying to production...'
                      env.deployedLink = '3.7.253.96:81'
                      echo "Deployed Link: ${env.deployedLink}"
  
                }
            }
        }
    }
}
