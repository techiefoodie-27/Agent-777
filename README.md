Agent 777

Agent 777 is a cybersecurity project that I'm building to bring different security tools and services together in one platform.

The idea is to have separate services for things like network scanning, log analysis and vulnerability checking, while using a central gateway to connect everything.

 Current Progress

- Gateway Service built with FastAPI
- API structure with `/api/v1`
- Gateway health check
- Network Scanner Service
- Gateway connected with the Network Scanner
- Shared schemas between services
- Docker Compose setup

 Planned

- Log Analyzer
- CVE / Vulnerability Lookup
- Security findings
- Alert system
- Dashboard
- Better monitoring and reporting

 Tech Stack

- Python
- FastAPI
- Pydantic
- Docker
- REST API
- Microservices

 Project Structure

```text
Agent-777/
│
├── services/
│   ├── gateway-service/
│   └── network-scanner-service/
│
├── shared/
│   └── schemas/
│
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE

Goal

The goal of Agent 777 is to build a practical cybersecurity platform where different security services can work together instead of having everything in one application.

This project is still under development.
