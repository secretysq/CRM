pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository'
                // 仓库已配置，Jenkins 会自动克隆
            }
        }
        stage('Build') {
            steps {
                echo 'Building project'
                // 示例：运行 Maven 构建
                // sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests'
                milestone(1) // 测试 pipeline-milestone-step 插件
                // 示例：运行测试
                // sh 'mvn test'
            }
        }
    }
}
