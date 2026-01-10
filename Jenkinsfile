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
                bat 'docker build -t personal-finance-tracker:ci .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic test'
                bat 'python --version'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage (demo)'
                bat 'echo Deploy completed'
            }
        }
    }
}

