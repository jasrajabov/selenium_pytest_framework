pipeline {
    agent any
    stages {
        stage('Set up env') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'python3 --version'
                sh 'pip3 install requirements.txt'
            }
        }
        stage('test') {

            steps {
                sh 'python3 -m pytest tests/main.py'
            }
            
        }
    }
}