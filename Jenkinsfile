pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "C:\\Users\\B00134339\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // No need for extra 'Clone Repo' if using `checkout scm`, but leaving your approach
                git branch: 'main', url: 'https://github.com/Gsodipo/fastapi-inventory-api'
            }
        }

        stage('Set Up Environment') {
            steps {
                // Create virtual env if it doesn’t exist (saves time!)
                bat """
                if not exist %VENV% (
                    %PYTHON% -m venv %VENV%
                )
                """
                // Only install dependencies if not already installed
                bat """
                %VENV%\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests & Generate PDF') {
            steps {
                bat '%VENV%\\Scripts\\activate && python generate_test_pdf.py'
            }
        }

        stage('Dump MongoDB') {
            steps {
                bat '%VENV%\\Scripts\\activate && python dump_mongodb_zip.py'
            }
        }

        stage('Create Final ZIP') {
            steps {
                // Avoid using fancy emojis in logs to prevent encoding crashes
                bat '%VENV%\\Scripts\\activate && python create_final_zip.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.pdf', fingerprint: true
            archiveArtifacts artifacts: 'complete-*.zip', fingerprint: true
        }
    }
}
