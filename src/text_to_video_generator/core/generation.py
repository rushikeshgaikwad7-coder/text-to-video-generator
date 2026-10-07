from datetime import datetime
from typing import Dict, Optional
from text_to_video_generator.api.schemas import JobStatus


class JobManager:
    """Manage generation jobs and their lifecycle."""
    
    def __init__(self):
        self.jobs: Dict[str, dict] = {}
    
    def create_job(self, job_id: str, mode: str, prompt: str, image_path: Optional[str], config: dict):
        """Create a new job."""
        self.jobs[job_id] = {
            "job_id": job_id,
            "mode": mode,
            "prompt": prompt,
            "image_path": image_path,
            "status": JobStatus.QUEUED,
            "progress": 0,
            "output": None,
            "error": None,
            "created_at": datetime.utcnow().isoformat(),
            "completed_at": None,
            "config": config
        }
    
    def get_job(self, job_id: str) -> Optional[dict]:
        """Get job details."""
        return self.jobs.get(job_id)
    
    def update_job_status(self, job_id: str, status: JobStatus, progress: int = None):
        """Update job status."""
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = status
            if progress is not None:
                self.jobs[job_id]["progress"] = min(progress, 100)
    
    def complete_job(self, job_id: str, output: dict):
        """Mark job as completed."""
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = JobStatus.COMPLETED
            self.jobs[job_id]["progress"] = 100
            self.jobs[job_id]["output"] = output
            self.jobs[job_id]["completed_at"] = datetime.utcnow().isoformat()
    
    def fail_job(self, job_id: str, error: str):
        """Mark job as failed."""
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = JobStatus.FAILED
            self.jobs[job_id]["error"] = error
            self.jobs[job_id]["completed_at"] = datetime.utcnow().isoformat()
