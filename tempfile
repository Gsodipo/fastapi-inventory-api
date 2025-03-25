pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Gsodipo/fastapi-inventory-api' // Replace with your real repo
            }
        }

        stage('Set up Virtual Env and Install Dependencies') {
            steps {
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests & Generate PDF') {
            steps {
                bat '%VENV%\\Scripts\\activate && python generate_test_pdf.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'unit_test_results.pdf', fingerprint: true
        }
    }
}
