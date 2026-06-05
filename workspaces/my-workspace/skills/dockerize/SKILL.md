---
name: "Dockerize"
description: "Create Dockerfile(s) and docker-compose templates; recommend multi-stage builds and image optimizations."
globs:
  - "Dockerfile"
  - "docker-compose.yml"
  - "compose.yaml"
---

# Dockerize

When invoked, generate Dockerfile(s) and optional `docker-compose.yml` tailored to the project:

- Provide a multi-stage Dockerfile (build + runtime) optimized for image size
- Recommend base images (alpine/slim variants) and non-root user
- Include `.dockerignore` suggestions and useful labels (org, version)
- Provide healthcheck, sensible ENTRYPOINT/CMD, and environment variable guidance
- Provide docker-compose example for local development with volumes and service dependencies
- Suggest build and push commands and CI integration notes

Example: multi-stage Node Dockerfile and compose file ready to use.