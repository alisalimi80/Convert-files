# Program purpuse
convert image file ro pdf

# Docker Compose Configuration

This repository contains a Docker Compose configuration that sets up a multi-container application for a Python-based project using FastAPI, Celery, Redis, and PostgreSQL.

## Overview

This Docker Compose configuration defines the services, networks, and volumes required to run a complete application with multiple components. The services include:

- **api**: FastAPI application server
- **worker**: Celery worker for background tasks
- **celery_beat**: Celery beat for scheduling periodic tasks
- **redis**: Redis database for message queuing and caching
- **database**: PostgreSQL database for storing application data

## Usage

To run the application, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
## Services

### api Service

Build: Uses the ./api directory to build the API service.

Ports: Maps port 80 of the host to port 8000 of the container.

Volumes: Mounts the ./api directory into the container's /usr/src/app.

Environment Variables:

CELERY_BROKER_URL: Redis URL for Celery message broker.

CELERY_RESULT_BACKEND: PostgreSQL URL for Celery result backend.

Dependencies: Depends on the redis and database services.

Networks: Connected to the ms_network network.

Command: Waits for the database to become available and starts the FastAPI app using uvicorn.
