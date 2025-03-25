pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Gsodipo/fastapi-inventory-api'
            }
        }

        stage('Set up Virtual Env and Install Dependencies') {
            steps {
                bat 'C:\\Users\\B00134339\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m venv %VENV%'
                bat '%VENV%\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests & Generate PDF') 
        {
            steps {
                bat '%VENV%\\Scripts\\activate && python generate_test_pdf.py'
            }
        }

        stage('Dump MongoDB and Zip') 
        {
            steps {
                bat 'venv\\Scripts\\activate && python dump_mongodb_zip.py'
            }
        }

        stage('Create Final ZIP')
        {
            steps {
                bat 'venv\\Scripts\\activate && python create_final_zip.py'
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'unit_test_results.pdf', fingerprint: true
            archiveArtifacts artifacts: 'complete-*.zip', fingerprint: true
        }
    }
}
