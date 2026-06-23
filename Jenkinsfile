pipeline {
    agent any

    environment {
        IMAGE_NAME = "devshree06/multitenant-expense"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

         stage('Deploy to Kubernetes') {
            steps {
                sh "/usr/local/bin/kubectl apply -f deployment.yaml -n uat"
                sh "/usr/local/bin/kubectl apply -f service.yaml -n uat"
                sh "/usr/local/bin/kubectl rollout restart deployment multitenant-expense -n uat"
            }
        }
    }
}