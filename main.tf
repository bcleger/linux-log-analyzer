terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "log_analyzer_container" {
  name     = "log-analyzer-container"
  image    = "log-analyzer"
  must_run = false

  command = ["sample.log"]
  
  rm = true
}