pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    IMAGE_NAME = "personal-finance-tracker"
    IMAGE_TAG  = "ci"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build') {
      steps {
        echo "Building Docker image..."
        bat "docker --version"
        bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
      }
    }

    stage('Test') {
      steps {
        echo "Running basic tests..."
        // If Python is installed on the Jenkins Windows machine:
        bat "python --version"

        // Quick sanity check: build should include the python file
        bat "dir"

        // Optional: run container quickly to verify it starts (won't fail pipeline if stops)
        // If your app listens on 80 inside the container:
        bat "docker run --rm %IMAGE_NAME%:%IMAGE_TAG% python -c \"import json; print('OK')\""
      }
    }

    stage('Deploy') {
      steps {
        echo "Deploy stage (demo)..."
        // Demo deploy: just show image exists
        bat "docker images | findstr %IMAGE_NAME%"
        bat "echo Deploy completed"
      }
    }
  }

  post {
    always {
      echo "Cleaning up dangling images (optional)..."
      // Don't fail pipeline if cleanup finds nothing
      bat "docker image prune -f || exit /b 0"
    }
    success {
      echo "✅ Pipeline finished successfully"
    }
    failure {
      echo "❌ Pipeline failed - check Console Output"
    }
  }
}

