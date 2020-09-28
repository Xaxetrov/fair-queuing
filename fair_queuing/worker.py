from fair_queuing.job import Job

class Worker():

    def __init__(self):
        self.current_job: Job = None
        self.current_queue = None
        self.finished_jobs = []
        self.spent_on_current_job = 0

    def process_current_job(self) -> bool:
        if self.current_job is None:
            return True

        self.spent_on_current_job += 1
        if self.spent_on_current_job == self.current_job.length:
            self.finished_jobs.append(self.current_job)
            self.current_job = None
            self.spent_on_current_job = 0
            return True