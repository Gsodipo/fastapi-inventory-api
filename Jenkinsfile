pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "C:\\Users\\B00134339\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Gsodipo/fastapi-inventory-api'
            }
        }

        stage('Set up Environment') {
            steps {
                bat """
                    if not exist %VENV% (
                        %PYTHON% -m venv %VENV%
                    )
                    %VENV%\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests & Generate PDF') {
            steps {
                bat '%VENV%\\Scripts\\python.exe generate_test_pdf.py'
            }
        }

        stage('Dump MongoDB') {
            steps {
                bat '%VENV%\\Scripts\\python.exe dump_mongodb_zip.py'
            }
        }

        stage('Create Final ZIP') {
            steps {
                bat '%VENV%\\Scripts\\python.exe create_final_zip.py'
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
