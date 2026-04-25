# ?? Linux Log Analyzer (Docker + Terraform)

A production-style project that analyzes Linux system logs and automates deployment using Infrastructure as Code.

---

## ?? Overview

This project demonstrates how to:

- Analyze Linux logs using Python
- Detect errors and failed SSH login attempts
- Containerize applications using Docker
- Automate deployment using Terraform

---

## ?? Tech Stack

- Python
- Docker
- Terraform (Infrastructure as Code)
- Linux log analysis

---

## ?? Features

- Detect system errors
- Identify failed SSH login attempts
- Extract and rank IP addresses
- CLI-based input
- JSON report generation
- Fully containerized
- Automated deployment with Terraform

---

## ?? How to Run (Docker)

```bash
docker build -t log-analyzer .
docker run log-analyzer sample.log

## Author
bcleger