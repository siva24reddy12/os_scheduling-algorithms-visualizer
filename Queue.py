from Process import *

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.size = 0
        self.rear = capacity - 1
        self.array = [None] * capacity

def is_full(selected_queue):
    return selected_queue.size + 1 == selected_queue.capacity

def is_empty(selected_queue):
    return selected_queue.size == 0

def enqueue(selected_queue, enqueuing_process):
    if is_full(selected_queue):
        return None
    selected_queue.rear = (selected_queue.rear + 1) % selected_queue.capacity
    selected_queue.array[selected_queue.rear] = enqueuing_process
    selected_queue.size += 1

def dequeue(selected_queue):
    if is_empty(selected_queue):
        return None
    dequeued_process = selected_queue.array[selected_queue.front]
    selected_queue.front = (selected_queue.front + 1) % selected_queue.capacity
    selected_queue.size -= 1
    return dequeued_process

def front(selected_queue):
    if is_empty(selected_queue):
        return None
    return selected_queue.array[selected_queue.front]

def rear(selected_queue):
    if is_empty(selected_queue):
        return None
    return selected_queue.array[selected_queue.rear]

def sort_queue_at(selected_queue):
    for i in range(selected_queue.size - 1):
        for j in range(selected_queue.size - i - 1):
            if selected_queue.array[j].arrival_time > selected_queue.array[j+1].arrival_time:
                selected_queue.array[j], selected_queue.array[j+1] = selected_queue.array[j+1], selected_queue.array[j]

def project_process_from_queue(selected_queue, selected_process):
    for i in range(selected_queue.size):
        if selected_queue.array[i].process_id == selected_process.process_id:
            return selected_queue.array[i]
    return None

def remove_process_from_queue(selected_queue, selected_process):
    for i in range(selected_queue.size):
        if selected_queue.array[i] == selected_process:
            for j in range(i, selected_queue.size - 1):
                selected_queue.array[j] = selected_queue.array[j + 1]
            selected_queue.size -= 1
            break
    selected_queue.rear -= 1

def get_process_with_minimum_CPU_burst_time(selected_queue):
    wanted_process = selected_queue.array[0]
    for i in range(1, selected_queue.size):
        if ((wanted_process.CPU_burst_time_1 != 0 and
             selected_queue.array[i].CPU_burst_time_1 != 0 and
             selected_queue.array[i].CPU_burst_time_1 < wanted_process.CPU_burst_time_1)
                or
            (wanted_process.CPU_burst_time_1 == 0 and
             selected_queue.array[i].CPU_burst_time_1 != 0 and
             selected_queue.array[i].CPU_burst_time_1 < wanted_process.CPU_burst_time_2)
                or
            (wanted_process.CPU_burst_time_1 != 0 and
             selected_queue.array[i].CPU_burst_time_1 == 0 and
             selected_queue.array[i].CPU_burst_time_2 < wanted_process.CPU_burst_time_1)
                or
            (wanted_process.CPU_burst_time_1 == 0 and
             selected_queue.array[i].CPU_burst_time_1 == 0 and
             selected_queue.array[i].CPU_burst_time_2 < wanted_process.CPU_burst_time_2)):

            wanted_process = selected_queue.array[i]
    return wanted_process

def get_process_with_highest_priority(selected_queue):
    wanted_process = selected_queue.array[0]
    for i in range(1, selected_queue.size):
        if wanted_process.priority_number < selected_queue.array[i].priority_number:
            wanted_process = selected_queue.array[i]
    return wanted_process

def remove_process_with_highest_priority(selected_queue):
    wanted_process = get_process_with_highest_priority(selected_queue)
    remove_process_from_queue(selected_queue, wanted_process)
    return wanted_process

def remove_process_with_minimum_CPU_burst_time(selected_queue):
    wanted_process = get_process_with_minimum_CPU_burst_time(selected_queue)
    remove_process_from_queue(selected_queue, wanted_process)
    return wanted_process

def copy_queue(selected_queue):
    new_queue = Queue(selected_queue.capacity)
    for i in range(selected_queue.size):
        enqueue(new_queue, copy_process(selected_queue.array[i]))
    return new_queue

def print_queue(selected_queue):
    print("\nProcesses in the queue:")
    for i in range(selected_queue.size):
        print_process(selected_queue.array[i])