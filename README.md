# Text-to-Video Generator

A modular, production-grade AI repository for generating videos from text or image prompts, with synchronized audio generation and export.

## Overview

This project is designed around a clean backend architecture for multimodal generation:

- Text-to-video generation
- Image-to-video generation
- Audio synthesis / ambient generation
- Video export pipeline
- FastAPI service for job submission and generation

The project intentionally separates concerns into modular components so it can evolve from a prototype to a real GPU-backed service.

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── src/
│   └── text_to_video_generator/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       ├── api/
│       │   ├── __init__.py
│       │   ├── routes.py
│       │   └── schemas.py
│       ├── audio/
│       │   ├── __init__.py
│       │   └── generator.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── factory.py
│       ├── pipelines/
│       │   ├── __init__.py
│       │   ├── text_to_video.py
│       │   ├── image_to_video.py
│       │   └── export.py
│       └── utils/
│           ├── __init__.py
│           ├── files.py
│           └── validators.py
├── tests/
│   └── test_api.py
└── outputs/
```

## Getting Started

### 1) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment

```bash
cp .env.example .env
```

### 4) Start the API

```bash
uvicorn text_to_video_generator.main:app --host 0.0.0.0 --port 8000 --reload
```

### 5) Call the API

```bash
curl -X POST "http://localhost:8000/generate/video" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A cinematic drone shot through a neon-lit city at night with reflections on wet streets",
    "duration_seconds": 6,
    "fps": 24,
    "width": 1280,
    "height": 720,
    "backend": "mock"
  }'
```

## Example Payloads

### Text-to-video

```json
{
  "prompt": "Sunrise over a mountain lake with gentle fog and warm golden light",
  "duration_seconds": 8,
  "fps": 24,
  "width": 1920,
  "height": 1080,
  "backend": "mock"
}
```

### Image-to-video

```json
{
  "image_path": "./samples/input.png",
  "prompt": "Slow camera push-in with subtle motion and cinematic lighting",
  "duration_seconds": 8,
  "fps": 24,
  "backend": "mock"
}
```

## Production Notes

This repository is structured to support real GPU-backed generation through Hugging Face Diffusers and PyTorch. The mock backend is included so the project can run locally without needing a large model download.

### Planned real backends

- Diffusers-based text-to-video models
- Image-to-video diffusion models
- Temporal consistency and frame interpolation enhancement
- Audio synchronization and soundtrack generation

## License

MIT
