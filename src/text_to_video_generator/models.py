from abc import ABC, abstractmethod
from typing import Any

from .config import VideoRequest


class VideoModel(ABC):
    """Interface for text-to-video models."""

    @abstractmethod
    def generate_video(self, request: VideoRequest) -> Any:
        raise NotImplementedError


class MockVideoModel(VideoModel):
    """A simple placeholder model used for tests and local development."""

    def generate_video(self, request: VideoRequest):
        return {
            "prompt": request.prompt,
            "duration_seconds": request.duration_seconds,
            "fps": request.fps,
            "resolution": f"{request.width}x{request.height}",
            "status": "mock_generated",
            "metadata": {
                "style": request.style,
                "negative_prompt": request.negative_prompt,
                "seed": request.seed,
            },
        }
