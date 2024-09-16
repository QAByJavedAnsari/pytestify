pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'pytestify:latest'
        ALLURE_RESULTS = 'allure-results'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from your repository (e.g., GitHub)
                git branch: 'main', url: 'https://github.com/qabyjavedansari/pytestify.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from the Dockerfile
                    DOCKER_IMAGE = docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                script {
                    // Run tests inside the built Docker container
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'poetry run pytest -m fintests --alluredir=allure-results --log-cli-level=INFO -s'
                    }
                }
            }
            post {
                always {
                    // Archive the Allure results regardless of test outcomes
                    archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
                }
            }
        }

        stage('Allure Report') {
            steps {
                script {
                    // Use the Allure plugin to generate and display the report
                    allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the pipeline finishes
            cleanWs()
        }
        failure {
            // Send a notification in case of failure (Optional: customize as per your setup)
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}
