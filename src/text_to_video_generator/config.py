from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GenerationConfig:
    output_dir: str = "output"
    fps: int = 24
    width: int = 1280
    height: int = 720
    duration_seconds: int = 5
    seed: Optional[int] = None
    negative_prompt: str = "blurry, low quality, distorted"


@dataclass
class VideoRequest:
    prompt: str
    duration_seconds: int = 5
    fps: int = 24
    width: int = 1280
    height: int = 720
    negative_prompt: str = "blurry, low quality, distorted"
    style: str = "cinematic"
    seed: Optional[int] = None
    metadata: dict = field(default_factory=dict)
