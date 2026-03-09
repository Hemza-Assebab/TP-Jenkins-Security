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
dependencyCheck additionalArguments: '--project TP-Jenkins --scan . --format HTML', 
                                odcInstallation: 'DP-Check'            }
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