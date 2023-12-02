from Process import get_process_waiting_time, get_process_turnaround_time

def analyze_processes_of_queue(terminated_queue, output_file):
    for i in range(terminated_queue.size):
        selected_process = terminated_queue.array[i]
        output_file.write(f"Process {selected_process.process_id}:\n")
        output_file.write(f"\tarrival time: {selected_process.arrival_time}\n")
        output_file.write(f"\ttermination time: {selected_process.termination_time}\n")
        output_file.write(f"\tresponse time: {selected_process.response_time}\n")
        output_file.write(f"\tturnaround time: {get_process_turnaround_time(selected_process)}\n")
        output_file.write(f"\twaiting time: {get_process_waiting_time(selected_process)}\n")
