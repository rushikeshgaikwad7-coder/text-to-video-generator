from fastapi import APIRouter, HTTPException

from text_to_video_generator.api.schemas import GenerationResponse, ImageToVideoRequest, TextToVideoRequest
from text_to_video_generator.pipelines.image_to_video import ImageToVideoPipeline
from text_to_video_generator.pipelines.text_to_video import TextToVideoPipeline

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok", "service": "text-to-video-generator"}


@router.post("/generate/video", response_model=GenerationResponse)
def generate_video(request: TextToVideoRequest):
    try:
        pipeline = TextToVideoPipeline(backend=request.backend, output_dir="outputs")
        result = pipeline.run(
            prompt=request.prompt,
            duration_seconds=request.duration_seconds,
            fps=request.fps,
            width=request.width,
            height=request.height,
            audio_enabled=request.audio_enabled,
        )
        return GenerationResponse(status="success", message="Video generation job completed", output=result)
    except Exception as exc:  # pragma: no cover - error path
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/generate/video-from-image", response_model=GenerationResponse)
def generate_video_from_image(request: ImageToVideoRequest):
    try:
        pipeline = ImageToVideoPipeline(backend=request.backend, output_dir="outputs")
        result = pipeline.run(
            image_path=request.image_path,
            prompt=request.prompt,
            duration_seconds=request.duration_seconds,
            fps=request.fps,
            width=request.width,
            height=request.height,
            audio_enabled=request.audio_enabled,
        )
        return GenerationResponse(status="success", message="Image-to-video generation job completed", output=result)
    except Exception as exc:  # pragma: no cover - error path
        raise HTTPException(status_code=500, detail=str(exc)) from exc
