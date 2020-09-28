from fair_queuing.job import Job
from fair_queuing.queue import Queue
from fair_queuing.worker import Worker

import math


# Data

queues = [
    Queue("Alpha", [0, 10, 20 ,30, 40, 50, 60, 70, 80, 90], [15, 12, 9, 18, 16, 11, 9, 8, 9, 15]),
    Queue("Bravo", [4, 5, 5 ,5, 50, 50, 60, 60, 60, 60], [6, 7, 7, 3, 10, 7, 7, 8, 40, 8]),
    Queue("Charly", [0, 10, 20], [20, 35, 20]),
]
worker = Worker()
t_max = 305


# Functions

def log(t: int, message: str):
    print("t=" + str(t) + " : " + message)


def add_jobs_to_queues(t: int):
    for queue in queues:
        while queue.next_job_to_arrive < len(queue.job_arrivals) and queue.job_arrivals[queue.next_job_to_arrive] == t:
            job = Job(queue.job_arrivals[queue.next_job_to_arrive], queue.job_lengths[queue.next_job_to_arrive])
            queue.jobs.append(job)
            queue.next_job_to_arrive += 1
            log(t, "Added job to queue " + queue.name + ". " + str(job))


def choose_queue(t) -> Queue:
    chosen_queue = None
    min_virtual_finish = math.inf
    for queue in queues:
        if (queue.next_job_to_process < len(queue.jobs)
            and queue.jobs[queue.next_job_to_process].virtual_finish < min_virtual_finish):
                min_virtual_finish = queue.jobs[queue.next_job_to_process].virtual_finish
                chosen_queue = queue

    return chosen_queue


def update_current_job(t: int):
    for queue in queues:
        queue.computeNextVirtualTimes()

    queue = choose_queue(t)

    if queue is None:
        log(t, "No job to take from queues")
        return
    else:
        log(t, "Next job to process taken from queue " + queue.name + ": " + str(queue.jobs[queue.next_job_to_process]))

    worker.current_queue = queue
    worker.current_job = queue.jobs[queue.next_job_to_process]
    queue.next_job_to_process += 1


# Main

t = 0
while t < t_max:
    add_jobs_to_queues(t)
    should_choose_job = worker.process_current_job()
    if should_choose_job:
        update_current_job(t)
    t += 1
    