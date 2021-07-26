pipeline {
    agent {
        docker {
            alwaysPull True
            image 'python:3.8'
        }
    }
    
    stages {
        stage('1. Environment Setup') {
            steps { 
                echo "=============="
                }
                stage('Build-test-2') {
                    steps{ build 'Build-test-2' }
                }
                stage('Build-test-3') {
                    steps{ build 'Build-test-3' }
                }
                stage('Build-test-4') {
                    steps { build 'Build-test-4'}
        }
    }
}
