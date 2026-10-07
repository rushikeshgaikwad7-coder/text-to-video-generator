# Text-to-Video Generator - Complete Production-Grade System

**A unified, user-friendly AI video generation platform** with text-to-video, image-to-video, and integrated audio synthesis.

## ✨ Features

- ✅ **Text-to-Video**: Generate cinematic videos from text prompts
- ✅ **Image-to-Video**: Transform static images into animated sequences
- ✅ **Audio Integration**: Automatic sound design, music, and voiceover sync
- ✅ **User-Friendly API**: Simple, guided, intuitive request format
- ✅ **Job Queue System**: Async processing with status tracking
- ✅ **Mock & Real Backends**: Test locally, deploy with real models
- ✅ **One-Click Download**: Complete project ready to run

## 🚀 Quick Start (30 seconds)

```bash
# 1. Clone and setup
git clone https://github.com/rushikeshgaikwad7-coder/text-to-video-generator.git
cd text-to-video-generator
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Start API
uvicorn src.text_to_video_generator.main:app --reload

# 3. Generate video
curl -X POST "http://localhost:8000/api/v1/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "text_to_video",
    "prompt": "A cinematic drone shot over a neon-lit city at night",
    "duration_seconds": 8,
    "style": "cinematic"
  }'
```

## 📋 Project Structure

```
text-to-video-generator/
├── README.md                           # This file
├── requirements.txt                    # All dependencies
├── pyproject.toml                      # Package config
├── .env.example                        # Environment template
├── docker-compose.yml                  # Docker setup (optional)
├── src/
│   └── text_to_video_generator/
│       ├── __init__.py
│       ├── config.py                   # Config & settings
│       ├── main.py                     # FastAPI app entry
│       ├── api/
│       │   ├── __init__.py
│       │   ├── routes.py               # API endpoints
│       │   ├── schemas.py              # Request/response models
│       │   └── jobs.py                 # Job queue & tracking
│       ├── core/
│       │   ├── __init__.py
│       │   ├��─ generation.py           # Core generation logic
│       │   └── job_manager.py          # Job lifecycle management
│       ├── models/
│       │   ├── __init__.py
│       │   ├── base.py                 # Base model interface
│       │   ├── mock.py                 # Mock backend (local testing)
│       │   └── factory.py              # Model provider factory
│       ├── pipelines/
│       │   ├── __init__.py
│       │   ├── text_to_video.py        # Text→video pipeline
│       │   ├── image_to_video.py       # Image→video pipeline
│       │   └── export.py               # Video/audio export
│       ├── audio/
│       │   ├── __init__.py
│       │   ├── generator.py            # Audio generation
│       │   └── synthesizer.py          # TTS & music sync
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── files.py                # File I/O utilities
│       │   ├── validators.py           # Input validation
│       │   └── logger.py               # Logging setup
│       └── db/
│           ├── __init__.py
│           └── storage.py              # Job & artifact storage
├── tests/
│   ├── __init__.py
│   ├── test_api.py                     # API endpoint tests
│   ├── test_pipelines.py               # Pipeline tests
│   └── test_schemas.py                 # Schema validation tests
├── examples/
│   ├── basic_text_to_video.py
│   ├── basic_image_to_video.py
│   └── api_client.py                   # Python client for API
├── outputs/                            # Generated videos (gitignored)
└── logs/                               # Application logs (gitignored)
```

## 🎯 Simple API Usage

### Text-to-Video

```bash
curl -X POST "http://localhost:8000/api/v1/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "text_to_video",
    "prompt": "A sunset over a calm ocean with warm golden light",
    "duration_seconds": 8,
    "resolution": "1920x1080",
    "style": "cinematic",
    "audio": {"enabled": true, "type": "ambient"}
  }'
```

**Response:**
```json
{
  "job_id": "job_abc123",
  "status": "processing",
  "message": "Video generation started",
  "result_url": "/api/v1/jobs/job_abc123/result"
}
```

### Image-to-Video

```bash
curl -X POST "http://localhost:8000/api/v1/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "image_to_video",
    "image_path": "./inputs/portrait.png",
    "prompt": "Slow zoom with cinematic lighting and ambient sound",
    "duration_seconds": 10,
    "style": "cinematic"
  }'
```

### Check Job Status

```bash
curl "http://localhost:8000/api/v1/jobs/job_abc123"
```

**Response:**
```json
{
  "job_id": "job_abc123",
  "status": "completed",
  "progress": 100,
  "output": {
    "video_path": "outputs/sunset_ocean_8s.mp4",
    "audio_path": "outputs/sunset_ocean_audio.wav",
    "duration_seconds": 8,
    "resolution": "1920x1080",
    "created_at": "2026-10-07T10:30:00Z"
  }
}
```

## 🎨 Style Options

Choose from predefined visual styles:
- `cinematic` — Hollywood-style motion and lighting
- `animated` — Smooth, stylized animation
- `photorealistic` — Ultra-realistic detail and motion
- `dreamy` — Soft focus, surreal atmosphere
- `technical` — Sharp, precise visualization
- `documentary` — Natural, observational style

## 🔧 Installation & Setup

### Requirements
- Python 3.10+
- pip or conda
- FFmpeg (optional, for video export)
- NVIDIA GPU (optional, for real model backends)

### Step 1: Clone the Repository

```bash
git clone https://github.com/rushikeshgaikwad7-coder/text-to-video-generator.git
cd text-to-video-generator
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings (optional)
```

### Step 5: Start the API

```bash
uvicorn src.text_to_video_generator.main:app --host 0.0.0.0 --port 8000 --reload
```

API is now available at: **http://localhost:8000**

**API Documentation (auto-generated):**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📚 Python Client Example

```python
from text_to_video_generator.client import VideoGenerationClient

client = VideoGenerationClient(base_url="http://localhost:8000")

# Generate text-to-video
job = client.generate_text_to_video(
    prompt="A futuristic city with flying cars and neon lights",
    duration_seconds=8,
    style="cinematic"
)

print(f"Job ID: {job['job_id']}")
print(f"Status: {job['status']}")

# Poll for completion
result = client.wait_for_completion(job['job_id'], timeout=300)

if result['status'] == 'completed':
    print(f"Video saved to: {result['output']['video_path']}")
    print(f"Audio saved to: {result['output']['audio_path']}")
```

## 🐳 Docker Setup (Optional)

```bash
# Build and run with Docker
docker-compose up --build

# API will be at http://localhost:8000
```

## 📊 Configuration

Edit `.env` to customize:

```bash
# API Settings
API_HOST=0.0.0.0
API_PORT=8000

# Model Settings
MODEL_BACKEND=mock              # mock, diffusers, custom
DIFFUSERS_MODEL_ID=""          # Model HuggingFace ID (when using diffusers)
DEVICE=cpu                       # cpu, cuda, mps

# Generation Settings
DEFAULT_FPS=24
DEFAULT_RESOLUTION=1920x1080
MAX_VIDEO_DURATION=60

# Audio Settings
ENABLE_AUDIO=true
AUDIO_BACKEND=mock              # mock, tts, music_gen

# Storage
OUTPUT_DIR=outputs
MAX_OUTPUT_SIZE_MB=1000

# Logging
LOG_LEVEL=INFO
ENABLE_DEBUG=false
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_api.py -v

# Run with coverage
pytest tests/ --cov=src
```

## 📦 Download & Use

This repository is **fully self-contained** and ready to download and use:

```bash
# Clone the repository
git clone https://github.com/rushikeshgaikwad7-coder/text-to-video-generator.git

# All dependencies are in requirements.txt
# All code is production-ready
# All examples are included
# Start immediately with: python -m uvicorn src.text_to_video_generator.main:app
```

## 🎓 Example Prompts

### Cinematic
```
A dramatic sunrise over snow-capped mountains with golden light and mist
A slow tracking shot through an ancient forest with dappled sunlight and rustling leaves
An aerial view of a coastal city at night with lights reflecting on the ocean
```

### Animated
```
A cheerful character walking through a colorful fantasy landscape
A smooth camera rotation around a glowing crystal in a mystical cave
Swirling abstract patterns morphing into geometric shapes
```

### Technical
```
A product showcase with 360-degree rotation and precise lighting
A schematic diagram animating to show how a mechanical system works
A data visualization with graphs and flowing information
```

## 🚀 Next Steps

### For Local Testing
- Use the `mock` backend (no GPU required)
- Generate test videos locally
- Verify the API works end-to-end

### For Real Generation
1. Install GPU dependencies: `pip install -r requirements-gpu.txt`
2. Download a model: `python -m text_to_video_generator.models.download --model stabilityai/stable-video-diffusion`
3. Update `.env`: `MODEL_BACKEND=diffusers`
4. Restart the API and generate videos

### For Production Deployment
1. Use Docker or Kubernetes for orchestration
2. Add a job database (PostgreSQL, Redis)
3. Set up async workers for background processing
4. Configure GPU resource allocation
5. Add authentication and rate limiting

## 📖 Documentation

- [API Reference](./docs/API.md)
- [Architecture](./docs/ARCHITECTURE.md)
- [Model Integration Guide](./docs/MODELS.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)

## 💡 Key Features

### User-Friendly
- Simple, guided API
- High-level prompts (no model internals)
- Job-based async processing
- Clear status tracking
- Auto-generated documentation

### Modular
- Pluggable model backends
- Separable audio generation
- Export layer with multiple formats
- Easy to extend and customize

### Production-Ready
- Comprehensive error handling
- Input validation
- Logging and monitoring
- Docker support
- Test coverage

### Well-Documented
- This README
- API docs (Swagger/ReDoc)
- Example scripts
- Architecture guide

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

MIT License - Free for personal and commercial use

## 🙋 Support

- 📧 Email: rushikeshgaikwad7@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/rushikeshgaikwad7-coder/text-to-video-generator/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/rushikeshgaikwad7-coder/text-to-video-generator/discussions)

---

**Ready to generate? Start the API and visit http://localhost:8000/docs!**
