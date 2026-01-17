import uuid
import time
from typing import Dict, Any, List, Optional
from enum import Enum
from pydantic import BaseModel

class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class Job(BaseModel):
    id: str
    status: JobStatus
    created_at: float
    result: Optional[Any] = None
    error: Optional[str] = None
    meta: Dict[str, Any] = {}

class JobManager:
    _instance = None
    _jobs: Dict[str, Job] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JobManager, cls).__new__(cls)
        return cls._instance

    def create_job(self, meta: Dict[str, Any] = {}) -> Job:
        job_id = str(uuid.uuid4())
        job = Job(
            id=job_id,
            status=JobStatus.QUEUED,
            created_at=time.time(),
            meta=meta
        )
        self._jobs[job_id] = job
        return job

    def get_job(self, job_id: str) -> Optional[Job]:
        return self._jobs.get(job_id)

    def update_job(self, job_id: str, status: JobStatus, result: Any = None, error: str = None):
        if job_id in self._jobs:
            job = self._jobs[job_id]
            job.status = status
            if result:
                job.result = result
            if error:
                job.error = error

    def list_jobs(self) -> List[Job]:
        return list(self._jobs.values())

# Global Instance
job_manager = JobManager()
