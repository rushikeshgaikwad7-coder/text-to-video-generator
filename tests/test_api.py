from fastapi.testclient import TestClient
from text_to_video_generator.main import app
import time

client = TestClient(app)


def test_health():
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_text_to_video_generation():
    payload = {
        "mode": "text_to_video",
        "prompt": "A neon-lit futuristic city",
        "duration_seconds": 5,
        "style": "cinematic"
    }
    r = client.post("/api/v1/generate", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "job_id" in data
    assert data["status"] == "queued"


def test_get_job_status():
    payload = {
        "mode": "text_to_video",
        "prompt": "A sunny beach",
        "duration_seconds": 5
    }
    r = client.post("/api/v1/generate", json=payload)
    job_id = r.json()["job_id"]
    
    time.sleep(0.5)
    
    r = client.get(f"/api/v1/jobs/{job_id}")
    assert r.status_code == 200
    assert r.json()["job_id"] == job_id


def test_examples():
    r = client.get("/api/v1/examples")
    assert r.status_code == 200
    assert "cinematic" in r.json()
