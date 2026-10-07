import argparse
from pathlib import Path

from .config import VideoRequest
from .models import MockVideoModel
from .pipeline import VideoGenerationPipeline


def main():
    parser = argparse.ArgumentParser(description="Generate a mock text-to-video artifact.")
    parser.add_argument("--prompt", required=True, help="Text prompt describing the video")
    parser.add_argument("--output", default="output/demo.mp4", help="Output video path")
    parser.add_argument("--duration", type=int, default=5, help="Video duration in seconds")
    parser.add_argument("--fps", type=int, default=24, help="Output video FPS")
    parser.add_argument("--width", type=int, default=1280, help="Output width in pixels")
    parser.add_argument("--height", type=int, default=720, help="Output height in pixels")
    parser.add_argument("--style", default="cinematic", help="Visual style")
    args = parser.parse_args()

    request = VideoRequest(
        prompt=args.prompt,
        duration_seconds=args.duration,
        fps=args.fps,
        width=args.width,
        height=args.height,
        style=args.style,
    )

    pipeline = VideoGenerationPipeline(model=MockVideoModel(), output_dir=str(Path(args.output).parent))
    response = pipeline.run(request, output_path=args.output)

    print(f"Generated video artifact at: {response['output_path']}")
    print(response["result"])


if __name__ == "__main__":
    main()
