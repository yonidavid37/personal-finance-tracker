# Personal Finance Tracker -- Kubernetes Deployment (v1.1)

A simple Flask application that loads financial data from a JSON file


## Prerequisites

Before deploying, ensure the following are installed:

 -   Minikube
 -   Kubectl
 -   Helm


## How to Run the Application (Helm + Kubernetes)

### 1. Start Minikube

    minikube start

### 2. Deploy the application using Helm

(From the folder containing the `finance-tracker/` chart)

    helm upgrade --install finance-tracker ./finance-tracker

### 3. Get the external URL to access the app

    minikube service finance-tracker --url

Open the returned URL in your browser to view the application.
