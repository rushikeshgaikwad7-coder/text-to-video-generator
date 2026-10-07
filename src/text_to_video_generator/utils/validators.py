from pathlib import Path
from typing import Any


def ensure_directory(path: str | Path) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def build_output_path(output_dir: str, file_name: str) -> str:
    directory = ensure_directory(output_dir)
    return str(directory / file_name)


def validate_prompt(prompt: str) -> str:
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    return prompt.strip()


def validate_image_path(image_path: str) -> str:
    if not image_path or not image_path.strip():
        raise ValueError("Image path cannot be empty")
    return image_path.strip()


def sanitize_filename(name: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in name).lower()
