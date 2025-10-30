pipeline {
    agent any

    environment {
        APP_PORT = "8501"
        VENV_DIR = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/PiyushDeshmukh-apperentice/Jenkins.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running basic sanity tests...'
                sh '''
                    source ${VENV_DIR}/bin/activate
                    python -m streamlit --version
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Starting Streamlit app...'
                sh '''
                    pkill -f "streamlit run" || true
                    nohup ${VENV_DIR}/bin/streamlit run app.py --server.port=${APP_PORT} --server.address=0.0.0.0 &
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! App is live on port ${APP_PORT}"
        }
        failure {
            echo "❌ Build or deployment failed."
        }
    }
}
