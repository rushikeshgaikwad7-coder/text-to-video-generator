from __future__ import annotations

from pathlib import Path

from text_to_video_generator.utils.files import build_output_path, sanitize_filename
from text_to_video_generator.pipelines.export import render_placeholder_audio, render_placeholder_video


class VideoExportPipeline:
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = output_dir

    def export_video(self, prompt: str, duration_seconds: int = 5, width: int = 1280, height: int = 720, audio_enabled: bool = True):
        slug = sanitize_filename(prompt)[:80] or "video"
        video_path = render_placeholder_video(self.output_dir, f"{slug}_{duration_seconds}s.mp4", duration=duration_seconds, width=width, height=height)

        audio_path = None
        if audio_enabled:
            audio_path = render_placeholder_audio(self.output_dir, f"{slug}_audio.wav", duration=duration_seconds)

        return {
            "video_path": video_path,
            "audio_path": audio_path,
            "duration_seconds": duration_seconds,
            "resolution": f"{width}x{height}",
            "status": "exported",
        }
