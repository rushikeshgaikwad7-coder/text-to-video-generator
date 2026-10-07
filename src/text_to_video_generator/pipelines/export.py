import subprocess
from pathlib import Path

from text_to_video_generator.utils.files import build_output_path


def render_placeholder_video(output_dir: str, file_name: str, duration: int = 5, width: int = 1280, height: int = 720) -> str:
    out_path = build_output_path(output_dir, file_name)
    ffmpeg_binary = "ffmpeg"
    try:
        subprocess.run(
            [
                ffmpeg_binary,
                "-y",
                "-f",
                "lavfi",
                "-i",
                f"color=c=black:s={width}x{height}:d={duration}",
                "-pix_fmt",
                "yuv420p",
                out_path,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return out_path
    except Exception:
        metadata_path = str(Path(out_path).with_suffix(".json"))
        with open(metadata_path, "w", encoding="utf-8") as fp:
            fp.write(
                {
                    "status": "placeholder_video_generated",
                    "output_path": out_path,
                    "duration_seconds": duration,
                    "resolution": f"{width}x{height}",
                    "note": "FFmpeg was not available; placeholder metadata was stored instead.",
                }
            )
        return metadata_path


def render_placeholder_audio(output_dir: str, file_name: str, duration: int = 5) -> str:
    out_path = build_output_path(output_dir, file_name)
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "lavfi",
                "-i",
                f"sine=frequency=440:duration={duration}",
                out_path,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return out_path
    except Exception:
        metadata_path = str(Path(out_path).with_suffix(".json"))
        with open(metadata_path, "w", encoding="utf-8") as fp:
            fp.write(
                {
                    "status": "placeholder_audio_generated",
                    "output_path": out_path,
                    "duration_seconds": duration,
                    "note": "FFmpeg was not available; placeholder metadata was stored instead.",
                }
            )
        return metadata_path
