from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from text_to_video_generator.config import VideoRequest
from text_to_video_generator.models import MockVideoModel
from text_to_video_generator.pipeline import VideoGenerationPipeline


def test_mock_generation_pipeline():
    request = VideoRequest(
        prompt="A futuristic city scene with flying cars and neon lights",
        duration_seconds=3,
        fps=24,
        width=1280,
        height=720,
    )

    pipeline = VideoGenerationPipeline(model=MockVideoModel(), output_dir="output")
    result = pipeline.run(request, output_path="output/test_output.mp4")

    assert result["result"]["status"] == "mock_generated"
    assert result["output_path"].endswith("test_output.mp4")
