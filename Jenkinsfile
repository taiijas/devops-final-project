pipeline {
   agent any

   environment {
       APP_NAME = "cloud-pulse-app"
       IMAGE_NAME = "cloud-pulse-app"
       IMAGE_TAG = "latest"
       AWS_HOST = "43.205.196.144"
       AWS_USER = "ubuntu"
       APP_PORT = "5000"
   }

   stages {
       stage('Checkout') {
           steps {
               echo 'Pulling source code from GitHub...'
               checkout scm
           }
       }

       stage('Build Docker Image') {
           steps {
               echo 'Building Docker image...'
               sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
           }
       }

       stage('Save Docker Image') {
           steps {
               echo 'Saving Docker image as tar file...'
               sh 'docker save ${IMAGE_NAME}:${IMAGE_TAG} -o ${IMAGE_NAME}.tar'
           }
       }

       stage('Copy Image to AWS') {
           steps {
               echo 'Copying Docker image to AWS server...'
               sh 'scp -o StrictHostKeyChecking=no ${IMAGE_NAME}.tar ${AWS_USER}@${AWS_HOST}:/home/ubuntu/'
           }
       }

       stage('Deploy on AWS') {
           steps {
               echo 'Deploying application on AWS server...'
               sh '''
               ssh -o StrictHostKeyChecking=no ${AWS_USER}@${AWS_HOST} "
                   docker stop ${APP_NAME} || true &&
                   docker rm ${APP_NAME} || true &&
                   docker load -i /home/ubuntu/${IMAGE_NAME}.tar &&
                   docker run -d \
                       --name ${APP_NAME} \
                       --restart unless-stopped \
                       -p ${APP_PORT}:5000 \
                       ${IMAGE_NAME}:${IMAGE_TAG}
               "
               '''
           }
       }

       stage('Verify Deployment') {
           steps {
               echo 'Checking application health endpoint...'
               sh 'sleep 5'
               sh 'curl -f http://${AWS_HOST}:${APP_PORT}/health'
           }
       }
   }

   post {
       success {
           echo 'Deployment completed successfully.'
       }

       failure {
           echo 'Deployment failed. Check Jenkins console output.'
       }
   }
}
