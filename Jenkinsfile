pipeline {
    agent any
    
    environment {
        name = 'gaurav'
    }
    
    parameters {
        string(name: 'person', defaultValue: 'Saurav Sharma', description: "Who are you?")
        booleanParam(name: 'isMale', defaultValue: true, description: "")
        choice(name: 'City', choices: ['Jaipur','Mumbai','Pune' ], description: "")
    }
    
    stages {
        stage('Run A command') {
            steps {
                sh '''
                ls
                date
                pwd
                cal 2021
                '''
            }
        }
        
        stage('Environment Variables') {
            steps {
                script {
                    env.username = 'myusername'
                    echo "${env.BUILD_ID}"
                    echo "${env.name}"
                    echo "${env.username}"
                }
            }
        }
        
        stage('Parameters') {
            steps {
                echo 'deploy on test'
                echo "${params.person}"
                echo "${params.isMale}"
            }
        }
        
        stage('Continue ?') {
            steps {
                script {
                    userInput = input(
                        id: 'userInput', message: 'Should we continue?', parameters: [
                            [$class: 'BooleanParameterDefinition', defaultValue: true, description: '']
                        ]
                    )
                    if (userInput) {
                        echo 'deploy on prod'
                    } else {
                        error('Aborted by user')
                    }
                }
            }
        }
        
        stage('Deploy on prod') {
            steps {
                echo 'deploy on prod'
            }
        }
    }
    
    post {
        always {
            echo 'I will always say Hello again!'
        }
        failure {
            echo 'Failure'
        }
        success {
            echo 'Success'
        }
    }
}
