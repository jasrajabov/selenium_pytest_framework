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

        stage('Converting xml to html') {
            steps {
                sh "python3 xml_to_html.py"
            }
        }
    }
    post {
        always {
            junit 'tests/junit/*.xml',
            emailext body: '${FILE,path="./tests/junit/email.html"}',
            to: 'razhabov@yahoo.com',
            subject: "Post ${BUILD_ID} notification",
        }
    }
}