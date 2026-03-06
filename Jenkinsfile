pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Hemza-Assebab/TP-Jenkins-Security.git'
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
                dependency-check \
                --project "TP-Jenkins" \
                --scan . \
                --format HTML \
                --failOnCVSS 7
                '''
            }
        }

        stage('SAST Scan') {
            steps {
                sh 'sonar-scanner'
            }
        }

    }

    post {
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}