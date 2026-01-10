pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t personal-finance-tracker:ci .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic test'
                sh 'python3 --version'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage (demo)'
                sh 'echo Deploy completed'
            }
        }
    }
}

