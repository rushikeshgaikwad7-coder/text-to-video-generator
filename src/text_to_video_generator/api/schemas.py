from __future__ import annotations

from text_to_video_generator.utils.files import build_output_path


def generate_background_audio(output_dir: str, prompt: str, duration_seconds: int = 5):
    file_name = f"{prompt[:30].replace(' ', '_').lower()}_audio.wav"
    path = build_output_path(output_dir, file_name)
    return {
        "path": path,
        "duration_seconds": duration_seconds,
        "style": "ambient",
        "note": "Audio generation is mocked. Replace with a real TTS/music model backend for production use.",
    }
