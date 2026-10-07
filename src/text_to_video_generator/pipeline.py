from pathlib import Path
from typing import Optional

from .config import VideoRequest
from .models import VideoModel


class VideoGenerationPipeline:
    def __init__(self, model: VideoModel, output_dir: str = "output"):
        self.model = model
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, request: VideoRequest, output_path: Optional[str] = None):
        result = self.model.generate_video(request)

        if output_path is None:
            file_name = "video_output.mp4"
            output_path = str(self.output_dir / file_name)

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Placeholder export: in a real project this writes the actual generated video.
        output_file.write_text(
            "# Placeholder video artifact\n"
            f"prompt={request.prompt}\n"
            f"duration={request.duration_seconds}\n"
            f"fps={request.fps}\n"
            f"size={request.width}x{request.height}\n",
            encoding="utf-8",
        )

        return {
            "output_path": str(output_file),
            "result": result,
        }
