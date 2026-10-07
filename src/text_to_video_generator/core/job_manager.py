from text_to_video_generator.api.schemas import GenerationRequest
from text_to_video_generator.core.job_manager import JobManager
from text_to_video_generator.models.factory import get_model
from text_to_video_generator.pipelines.text_to_video import TextToVideoPipeline
from text_to_video_generator.pipelines.image_to_video import ImageToVideoPipeline
import logging

logger = logging.getLogger(__name__)
job_manager = JobManager()


class GenerationEngine:
    """Core video generation engine."""
    
    def __init__(self):
        self.model = get_model(backend="mock")
    
    def generate(self, job_id: str, request: GenerationRequest):
        """Generate video for a job."""
        try:
            job_manager.update_job_status(job_id, "processing", progress=10)
            
            if request.mode == "text_to_video":
                pipeline = TextToVideoPipeline(backend="mock", output_dir="outputs")
                result = pipeline.run(
                    prompt=request.prompt,
                    duration_seconds=request.duration_seconds,
                    fps=request.fps,
                    width=int(request.resolution.split('x')[0]),
                    height=int(request.resolution.split('x')[1]),
                    audio_enabled=request.audio.enabled
                )
            elif request.mode == "image_to_video":
                pipeline = ImageToVideoPipeline(backend="mock", output_dir="outputs")
                result = pipeline.run(
                    image_path=request.image_path,
                    prompt=request.prompt,
                    duration_seconds=request.duration_seconds,
                    fps=request.fps,
                    width=int(request.resolution.split('x')[0]),
                    height=int(request.resolution.split('x')[1]),
                    audio_enabled=request.audio.enabled
                )
            else:
                raise ValueError(f"Unsupported mode: {request.mode}")
            
            job_manager.update_job_status(job_id, "processing", progress=90)
            job_manager.complete_job(job_id, output=result)
            logger.info(f"Job {job_id} completed successfully")
        
        except Exception as exc:
            logger.error(f"Job {job_id} failed: {str(exc)}")
            job_manager.fail_job(job_id, error=str(exc))
