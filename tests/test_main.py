from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_read_root_returns_project_metadata():
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {
        "project": "DevSecOps GitOps Platform",
        "message": "API is running successfully",
        "version": "1.0.0",
        "docs_url": "/docs",
        "health_check": "/health",
    }


def test_health_check_returns_service_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {
        "status": "healthy",
        "service": "devsecops-gitops-platform",
        "version": "1.0.0",
    }


def test_openapi_schema_exposes_application_metadata():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "DevSecOps GitOps Platform"
    assert schema["info"]["version"] == "1.0.0"
    assert "/" in schema["paths"]
    assert "/health" in schema["paths"]
