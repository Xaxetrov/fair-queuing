from fair_queuing.job import Job

from typing import List


class Queue():
    def __init__(self, name, job_arrivals, job_lengths):
        self.name = name
        self.job_arrivals = job_arrivals
        self.job_lengths = job_lengths

        self.next_job_to_arrive = 0
        self.next_job_to_process = 0

        self.jobs: List[Job] = []

        self.last_virtual_finish = 0
        self.estimated_job_length = 10

    def computeNextVirtualTimes(self):
        if self.next_job_to_process >= len(self.jobs):
            return

        if self.next_job_to_process >= 1:
            self.estimated_job_length = (self.estimated_job_length + self.jobs[self.next_job_to_process - 1].length) / 2

        next_job = self.jobs[self.next_job_to_process]
        next_job.virtual_start = max(next_job.arrival, self.last_virtual_finish)
        next_job.virtual_finish = next_job.virtual_start + self.estimated_job_length
