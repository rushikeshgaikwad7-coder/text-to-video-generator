from text_to_video_generator.models.base import MockVideoModel


def get_model(backend: str = "mock"):
    backend_key = (backend or "mock").lower()

    if backend_key in {"mock", "default"}:
        return MockVideoModel()

    raise ValueError(f"Unsupported backend: {backend}")
