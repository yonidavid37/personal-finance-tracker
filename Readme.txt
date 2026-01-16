# Personal Finance Tracker -- Kubernetes Deployment (v1.1)

A simple Flask application that loads financial data from a JSON file
UI refreshed using templates and basic styling.


## Prerequisites

Before deploying, ensure the following are installed:

 -   Minikube
 -   Kubectl
 -   Docker


## How to Run the Application 

### 1. Start Minikube

    minikube start


### 2. Deploy the application using Kubernetes

   kubectl apply -f finance-tracker/templates/


### 3. Get the external URL to access the app

   minikube service pft-finance-tracker --url
 

Open the returned URL in your browser to view the application.
