pipeline {
    agent any
    stages {
        stage('Set up env') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt --user'
            }
        }
        stage('Test') {

            steps {
                sh "python3 -m pytest tests/main_tests.py --junitxml='tests/junit/result.xml'"
            }
            
        }
    }
    post {
        always {
            junit 'tests/junit/*.xml'
        }
    }
}