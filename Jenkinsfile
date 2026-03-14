pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
                dependency-check.sh \
                --project "TP-Jenkins" \
                --scan . \
                --format HTML \
                --failOnCVSS 7
                '''
            }
        }
    }
}