#!/usr/bin/env python
"""Simple Python client for the API."""

import requests
import time
from typing import Optional


class VideoGenerationClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def generate_text_to_video(
        self,
        prompt: str,
        duration_seconds: int = 8,
        style: str = "cinematic",
        resolution: str = "1920x1080",
        fps: int = 24,
        audio: bool = True
    ) -> dict:
        """Generate video from text prompt."""
        payload = {
            "mode": "text_to_video",
            "prompt": prompt,
            "duration_seconds": duration_seconds,
            "style": style,
            "resolution": resolution,
            "fps": fps,
            "audio": {"enabled": audio}
        }
        r = requests.post(f"{self.base_url}/api/v1/generate", json=payload)
        r.raise_for_status()
        return r.json()
    
    def generate_image_to_video(
        self,
        image_path: str,
        prompt: str,
        duration_seconds: int = 8,
        style: str = "cinematic"
    ) -> dict:
        """Generate video from image."""
        payload = {
            "mode": "image_to_video",
            "image_path": image_path,
            "prompt": prompt,
            "duration_seconds": duration_seconds,
            "style": style,
            "audio": {"enabled": True}
        }
        r = requests.post(f"{self.base_url}/api/v1/generate", json=payload)
        r.raise_for_status()
        return r.json()
    
    def get_job_status(self, job_id: str) -> dict:
        """Get status of a job."""
        r = requests.get(f"{self.base_url}/api/v1/jobs/{job_id}")
        r.raise_for_status()
        return r.json()
    
    def wait_for_completion(self, job_id: str, timeout: int = 300, poll_interval: int = 2) -> dict:
        """Poll job status until completion."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            job = self.get_job_status(job_id)
            if job["status"] in ["completed", "failed"]:
                return job
            print(f"[{job['status'].upper()}] Progress: {job['progress']}%")
            time.sleep(poll_interval)
        raise TimeoutError(f"Job {job_id} timed out after {timeout} seconds")


if __name__ == "__main__":
    client = VideoGenerationClient()
    
    print("Generating video...")
    job = client.generate_text_to_video(
        prompt="A cinematic drone shot over a neon-lit city at night",
        duration_seconds=8,
        style="cinematic"
    )
    print(f"Job ID: {job['job_id']}")
    
    print("Waiting for completion...")
    result = client.wait_for_completion(job['job_id'])
    
    if result['status'] == 'completed':
        print(f"\nSuccess! Video saved to: {result['output']['export']['video_path']}")
    else:
        print(f"\nFailed: {result.get('error')}")
