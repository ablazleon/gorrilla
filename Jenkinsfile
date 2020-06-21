pipeline {
     agent any
     stages {
          stage ("Py3 Linting Check") {
              steps {
                  script {
                      env.lint3_result = "FAILURE"
                  }
                  bbcGithubNotify(context: "lint/flake8_3", status: "PENDING")
                  // Run the linter
                  sh 'python3 -m flake8'
                  script {
                      env.lint3_result = "SUCCESS" // This will only run if the sh above succeeded
                  }
              }
              post {
                  always {
                      bbcGithubNotify(context: "lint/flake8_3", status: env.lint3_result)
                  }
              }
          }                     
     }
}
