pipeline {
  agent any

  environment {
    IMAGE_NAME = "personal-finance-tracker:ci"
    // Change this if your manifests are in a different folder:
    MANIFEST_DIR = "K8S"
    // If your deployment name/service name differ, adjust:
    DEPLOYMENT_NAME = "pft-finance-tracker"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build') {
      steps {
        echo "Building Docker image..."
        bat 'docker --version'
        bat "docker build -t %IMAGE_NAME% ."
      }
    }

    stage('Test') {
      steps {
        echo "Running basic tests..."
        bat 'python --version'
        // simple container sanity check
        bat 'docker run --rm %IMAGE_NAME% python -c "print(\'OK\')"'
      }
    }

    stage('Deploy to Minikube') {
      steps {
        echo "Deploying to Minikube..."
        bat 'kubectl version --client'
        bat 'minikube status'

        // Make the locally-built image available inside Minikube
        bat "minikube image load %IMAGE_NAME%"

        // Apply Kubernetes manifests
        bat "kubectl apply -f %MANIFEST_DIR%"

        // Wait for rollout
        bat "kubectl rollout status deployment/%DEPLOYMENT_NAME% --timeout=180s"

        // Show what is running
        bat "kubectl get pods,svc"
      }
    }
  }

  post {
    always {
      echo "Pipeline finished"
    }
  }
}

