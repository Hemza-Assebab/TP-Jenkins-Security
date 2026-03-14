pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Hemza-Assebab/TP-Jenkins-Security.git'
            }
        }

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