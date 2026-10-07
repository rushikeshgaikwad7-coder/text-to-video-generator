from fastapi import APIRouter, HTTPException, BackgroundTasks
from text_to_video_generator.api.schemas import GenerationRequest, GenerationResponse, JobStatus
from text_to_video_generator.core.job_manager import JobManager
from text_to_video_generator.core.generation import GenerationEngine
import uuid
from datetime import datetime

router = APIRouter(prefix="/api/v1", tags=["generation"])
job_manager = JobManager()
generation_engine = GenerationEngine()


@router.get("/health")
def health_check():
    """Check if API is running."""
    return {
        "status": "ok",
        "service": "text-to-video-generator",
        "version": "0.1.0"
    }


@router.post("/generate", response_model=GenerationResponse)
def generate_video(request: GenerationRequest, background_tasks: BackgroundTasks):
    """Generate a video asynchronously."""
    try:
        job_id = str(uuid.uuid4())
        
        job_manager.create_job(
            job_id=job_id,
            mode=request.mode,
            prompt=request.prompt,
            image_path=request.image_path,
            config=request.dict()
        )
        
        background_tasks.add_task(
            generation_engine.generate,
            job_id,
            request
        )
        
        return GenerationResponse(
            job_id=job_id,
            status=JobStatus.QUEUED,
            message="Video generation job queued",
            result_url=f"/api/v1/jobs/{job_id}/result",
            progress=0
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/jobs/{job_id}")
def get_job_status(job_id: str):
    """Get the status of a generation job."""
    job = job_manager.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.get("/jobs/{job_id}/result")
def get_job_result(job_id: str):
    """Get the result of a completed job."""
    job = job_manager.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if job["status"] == JobStatus.PROCESSING:
        raise HTTPException(status_code=202, detail="Job is still processing")
    
    if job["status"] == JobStatus.FAILED:
        raise HTTPException(status_code=400, detail=job.get("error", "Generation failed"))
    
    return job


@router.get("/models")
def list_available_models():
    """List available generation models."""
    return {
        "models": [
            {"name": "mock", "description": "Mock backend for testing", "requires_gpu": False},
            {"name": "diffusers", "description": "HuggingFace Diffusers", "requires_gpu": True},
        ],
        "styles": ["cinematic", "animated", "photorealistic", "dreamy", "technical", "documentary"]
    }


@router.get("/examples")
def get_example_prompts():
    """Get example prompts for inspiration."""
    return {
        "cinematic": [
            "A dramatic sunrise over snow-capped mountains with golden light",
            "A slow tracking shot through an ancient forest with dappled sunlight",
            "An aerial view of a coastal city at night with ocean reflections"
        ],
        "animated": [
            "A cheerful character walking through a colorful fantasy landscape",
            "A smooth camera rotation around a glowing crystal in a cave",
            "Swirling abstract patterns morphing into geometric shapes"
        ],
        "technical": [
            "A product showcase with 360-degree rotation and precise lighting",
            "A schematic diagram showing how a mechanical system works",
            "A data visualization with flowing information and graphs"
        ]
    }
