from text_to_video_generator.config import VideoRequest
from text_to_video_generator.models import MockVideoModel
from text_to_video_generator.pipeline import VideoGenerationPipeline


if __name__ == "__main__":
    request = VideoRequest(
        prompt="A cinematic drone shot over a neon-lit city at night, reflection on wet asphalt, dramatic motion, high detail",
        duration_seconds=5,
        fps=24,
        width=1280,
        height=720,
        style="cinematic",
    )

    pipeline = VideoGenerationPipeline(model=MockVideoModel(), output_dir="output")
    response = pipeline.run(request, output_path="output/example_output.mp4")
    print(response)
