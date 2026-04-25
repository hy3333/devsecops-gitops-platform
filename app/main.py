from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="DevSecOps GitOps Platform",
    description="A hands-on project to learn and build a real-world DevOps workflow using FastAPI, Docker, Kubernetes, CI/CD, security scanning, and monitoring.",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
def read_root():
    return JSONResponse(
        content={
            "project": "DevSecOps GitOps Platform",
            "message": "API is running successfully",
            "version": "1.0.0",
            "docs_url": "/docs",
            "health_check": "/health",
        }
    )


@app.get("/health", tags=["Health"])
def health_check():
    return JSONResponse(
        content={
            "status": "healthy",
            "service": "devsecops-gitops-platform",
            "version": "1.0.0",
        }
    )