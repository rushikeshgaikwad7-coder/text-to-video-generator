from pathlib import Path
from text_to_video_generator.utils.files import build_output_path, sanitize_filename


class VideoExportPipeline:
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = output_dir
    
    def export_video(self, prompt: str, duration_seconds: int = 5, width: int = 1280, height: int = 720, audio_enabled: bool = True):
        slug = sanitize_filename(prompt)[:80] or "video"
        video_path = build_output_path(self.output_dir, f"{slug}_{duration_seconds}s.mp4")
        
        audio_path = None
        if audio_enabled:
            audio_path = build_output_path(self.output_dir, f"{slug}_audio.wav")
        
        return {
            "video_path": video_path,
            "audio_path": audio_path,
            "duration_seconds": duration_seconds,
            "resolution": f"{width}x{height}",
            "status": "ready"
        }
