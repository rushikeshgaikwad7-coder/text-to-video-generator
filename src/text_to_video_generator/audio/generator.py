from __future__ import annotations

from text_to_video_generator.models.factory import get_model
from text_to_video_generator.pipelines.export import VideoExportPipeline
from text_to_video_generator.utils.files import validate_image_path, validate_prompt


class ImageToVideoPipeline:
    def __init__(self, backend: str = "mock", output_dir: str = "outputs"):
        self.model = get_model(backend)
        self.exporter = VideoExportPipeline(output_dir=output_dir)

    def run(self, image_path: str, prompt: str, duration_seconds: int = 5, fps: int = 24, width: int = 1280, height: int = 720, audio_enabled: bool = True):
        clean_image = validate_image_path(image_path)
        clean_prompt = validate_prompt(prompt)
        generation = self.model.generate_image_to_video(clean_image, clean_prompt, duration_seconds=duration_seconds, fps=fps, width=width, height=height)
        export_result = self.exporter.export_video(clean_prompt, duration_seconds, width, height, audio_enabled=audio_enabled)
        return {
            "image_path": clean_image,
            "prompt": clean_prompt,
            "generation": generation,
            "export": export_result,
        }
