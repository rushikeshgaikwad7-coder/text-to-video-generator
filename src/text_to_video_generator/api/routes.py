from pydantic import BaseModel, Field


class TextToVideoRequest(BaseModel):
    prompt: str = Field(..., min_length=3)
    duration_seconds: int = Field(default=5, ge=1, le=60)
    fps: int = Field(default=24, ge=1, le=60)
    width: int = Field(default=1280, ge=256, le=3840)
    height: int = Field(default=720, ge=256, le=2160)
    backend: str = "mock"
    audio_enabled: bool = True


class ImageToVideoRequest(BaseModel):
    image_path: str = Field(...)
    prompt: str = Field(..., min_length=3)
    duration_seconds: int = Field(default=5, ge=1, le=60)
    fps: int = Field(default=24, ge=1, le=60)
    width: int = Field(default=1280, ge=256, le=3840)
    height: int = Field(default=720, ge=256, le=2160)
    backend: str = "mock"
    audio_enabled: bool = True


class GenerationResponse(BaseModel):
    status: str
    message: str
    output: dict
