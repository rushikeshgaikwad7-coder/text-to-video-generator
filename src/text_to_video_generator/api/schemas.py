from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class AudioType(str, Enum):
    AMBIENT = "ambient"
    MUSIC = "music"
    VOICEOVER = "voiceover"
    SILENCE = "silence"


class AudioConfig(BaseModel):
    enabled: bool = True
    type: AudioType = AudioType.AMBIENT
    volume: float = Field(default=0.7, ge=0.0, le=1.0)
    description: Optional[str] = None


class Style(str, Enum):
    CINEMATIC = "cinematic"
    ANIMATED = "animated"
    PHOTOREALISTIC = "photorealistic"
    DREAMY = "dreamy"
    TECHNICAL = "technical"
    DOCUMENTARY = "documentary"


class Resolution(str, Enum):
    SD = "1280x720"
    HD = "1920x1080"
    UHD = "3840x2160"
    CUSTOM = "custom"


class GenerationRequest(BaseModel):
    """User-friendly generation request."""
    mode: Literal["text_to_video", "image_to_video", "video_to_video"] = Field(..., description="Generation mode")
    prompt: str = Field(..., min_length=3, max_length=2000, description="Text prompt describing the video")
    image_path: Optional[str] = Field(None, description="Path to input image (required for image_to_video)")
    duration_seconds: int = Field(default=8, ge=1, le=60, description="Video duration in seconds")
    resolution: str = Field(default="1920x1080", description="Output resolution (WIDTHxHEIGHT)")
    fps: int = Field(default=24, ge=1, le=60, description="Frames per second")
    style: Style = Field(default=Style.CINEMATIC, description="Visual style")
    audio: AudioConfig = Field(default_factory=AudioConfig, description="Audio configuration")
    seed: Optional[int] = None


class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class GenerationResponse(BaseModel):
    """Simple generation response."""
    job_id: str
    status: JobStatus
    message: str
    result_url: Optional[str] = None
    progress: int = 0


class JobResult(BaseModel):
    """Job completion result."""
    job_id: str
    status: JobStatus
    progress: int
    output: Optional[dict] = None
    error: Optional[str] = None
    created_at: str
    completed_at: Optional[str] = None
