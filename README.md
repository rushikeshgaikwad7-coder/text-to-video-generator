# Text-to-Video Generator

A complete starter project for building AI-driven text-to-video generation systems. This repo provides a clean architecture for prompt processing, model abstraction, generation pipeline orchestration, and export to video files.

## Features

- Text-to-video request schema
- Model abstraction for diffusion and video generation providers
- Prompt normalization and generation options
- Local mock generator for development and testing
- CLI for generating sample videos
- Easy extension points for real model providers (Runway, Kling, Wan, LTX, etc.)

## Project Structure

```text
text-to-video-generator/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── examples/
│   └── basic_prompt.py
├── src/
│   └── text_to_video_generator/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       └── pipeline.py
└── tests/
    └── test_pipeline.py
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m text_to_video_generator.cli generate \
  --prompt "A cinematic drone shot over a neon-lit city at night, rain reflecting on the streets" \
  --output output/demo.mp4 \
  --duration 5
```

## Configuration

The project can be adapted to use different generation backends via the `VideoModel` interface. A default `MockVideoModel` is included for testing and local development.

## Extending the Project

To integrate a real provider:

1. Create a new class implementing `VideoModel`
2. Implement `generate_video(request)`
3. Add provider credentials to config
4. Update the CLI or pipeline selection logic

## Example Prompt

```text
A slow cinematic camera move through a desert canyon at sunrise, warm light, dust particles, ultra-detailed environment, realistic motion
```

## License

MIT
