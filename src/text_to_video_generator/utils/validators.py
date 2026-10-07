from pathlib import Path


def validate_file_exists(path: str) -> bool:
    return Path(path).exists()
