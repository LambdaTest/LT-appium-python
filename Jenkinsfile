pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/prashantsharma2608/LT-appium-python.git']]])
      }
    }

    stage('Test') {
      steps {
        bat 'pip install -r requirements.txt'
        // bat 'python -m pip install pytest'
      }
    }
    stage('Download LambdaTest Tunnel') {
    steps {
        bat 'wget https://downloads.lambdatest.com/tunnel/v3/linux/64bit/LT_Linux.zip'
        bat 'unzip lambdatest-tunnel.zip'
       }
    }
stage('Start LambdaTest Tunnel') {
    steps {
        bat './lambdatest-tunnel --user prashantsharma --key RlEUtZdSXJkl3iEtXNx6eWFSyLBfDJlkYRYG1igfb1OjpXfXRp'
       }
    }
    stage('run program') {
    steps {
        bat python android.py
       }
    }

stage('Stop LambdaTest Tunnel') {
    steps {
        sh './lambdatest-tunnel --user prashantsharma --key RlEUtZdSXJkl3iEtXNx6eWFSyLBfDJlkYRYG1igfb1OjpXfXRp --kill'
       }
   }

    stage('Report'){
      steps{
        lambdaTestReportPublisher 'automation'
      }
    }
  }
}
