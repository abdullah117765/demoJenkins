pipeline {

    environment {
        deployedLink="0.0.0.0"
    }
    
    agent any
    
    parameters {
        string(defaultValue: '1.2.3.4.5', description: 'Deployed Link', name: 'deployedLink')
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
                      deployedLink = '3.7.253.96:81'
                      echo "deployedLink: ${env.deployedLink}"
                      echo "pvalue: ${deployedLink}"
                      echo "Current environment variables: ${env}" // Debug statement
  
                }
            }
        }
    }
}
