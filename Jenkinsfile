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
        bat 'python android.py'
      }
    }
    stage('Report'){
      steps{
        lambdaTestReportPublisher 'automation'
      }
    }
  }
}
