pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
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
                --project TP-Jenkins \
                --scan . \
                --format HTML \
                --failOnCVSS 7 \
                --data /opt/dependency-check/data
                '''
            }
        }

        stage('SAST Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('Sonar') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectKey=tp-jenkins \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000
                        """
                    }
                }
            }
        }

    }

    post {
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}