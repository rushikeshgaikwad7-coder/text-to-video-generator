from text_to_video_generator.api.schemas import GenerationRequest, AudioConfig, Style
from text_to_video_generator.core.generation import GenerationEngine


if __name__ == "__main__":
    request = GenerationRequest(
        mode="text_to_video",
        prompt="A cinematic sunrise over mountains with golden light",
        duration_seconds=8,
        resolution="1920x1080",
        style=Style.CINEMATIC,
        audio=AudioConfig(enabled=True, type="ambient")
    )
    
    engine = GenerationEngine()
    print("Starting generation...")
    # In real app, this runs in background
    print(f"Request: {request}")
    print("Check http://localhost:8000/api/v1/jobs/[job_id] for status")
