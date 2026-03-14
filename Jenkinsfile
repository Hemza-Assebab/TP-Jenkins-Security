pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
                /opt/dependency-check/bin/dependency-check.sh \
                --project "TP-Jenkins" \
                --scan . \
                --format HTML \
                --out dependency-check-report \
                --failOnCVSS 7
                '''
            }
        }

    }

    post {
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}