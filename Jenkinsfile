pipeline {
    agent { label 'JenkinsSlave03' }  // Specify the agent here
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub')
    }
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t mohamedessam1911/weather-app-jenkins:latest .'
                }
            }
        }
        
        stage('Docker Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push mohamedessam1911/weather-app-jenkins:latest'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {

                    sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
