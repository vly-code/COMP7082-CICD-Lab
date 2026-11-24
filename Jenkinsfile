pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install pytest
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=report.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}

The virtual environment keeps pytest out of the system Python and inside the job's workspace. On a Windows node, use bat instead of sh:

groovy
bat '''
    python -m venv venv
    venv\\Scripts\\activate
    pip install pytest
    pytest --junitxml=report.xml
'''
