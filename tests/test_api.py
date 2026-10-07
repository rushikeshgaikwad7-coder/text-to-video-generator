from fastapi.testclient import TestClient

from text_to_video_generator.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_text_generation():
    payload = {
        "prompt": "A neon-lit futuristic city at night",
        "duration_seconds": 4,
        "fps": 24,
        "width": 1280,
        "height": 720,
        "backend": "mock",
        "audio_enabled": True,
    }
    r = client.post("/generate/video", json=payload)
    assert r.status_code == 200
    assert r.json()["status"] == "success"
