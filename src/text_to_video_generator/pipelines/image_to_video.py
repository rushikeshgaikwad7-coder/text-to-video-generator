from __future__ import annotations

from text_to_video_generator.models.base import MockVideoModel
from text_to_video_generator.models.factory import get_model
from text_to_video_generator.pipelines.export import VideoExportPipeline
from text_to_video_generator.utils.files import validate_prompt


class TextToVideoPipeline:
    def __init__(self, backend: str = "mock", output_dir: str = "outputs"):
        self.model = get_model(backend)
        self.exporter = VideoExportPipeline(output_dir=output_dir)

    def run(self, prompt: str, duration_seconds: int = 5, fps: int = 24, width: int = 1280, height: int = 720, audio_enabled: bool = True):
        clean_prompt = validate_prompt(prompt)
        generation = self.model.generate_text_to_video(clean_prompt, duration_seconds=duration_seconds, fps=fps, width=width, height=height)
        export_result = self.exporter.export_video(clean_prompt, duration_seconds, width, height, audio_enabled=audio_enabled)
        return {
            "prompt": clean_prompt,
            "generation": generation,
            "export": export_result,
        }
