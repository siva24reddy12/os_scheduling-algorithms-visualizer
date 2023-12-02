import matplotlib.pyplot as plt

file_path = 'output\FCFS\FCFS_Algorithms_Analysis.txt'

# Read the data from the text file
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit(1)

# Check for the expected structure
if not all(line.startswith('*') or line.startswith('Algorithm Analysis:') for line in lines[:3]):
    print("Error: Invalid file structure.")
    exit(1)

# Process the data
cpu_execution_time = int(lines[3].split(': ')[1].strip())
cpu_idle_time = int(lines[5].split(': ')[1].strip())
cpu_utilization = float(lines[7].split(': ')[1].strip()[:-1])
throughput = float(lines[9].split(': ')[1].strip())
average_turnaround_time = float(lines[11].split(': ')[1].strip())
average_waiting_time = float(lines[13].split(': ')[1].strip())
average_response_time = float(lines[15].split(': ')[1].strip())

# Create a bar graph
categories = ['CPU Execution Time', 'CPU Idle Time', 'CPU Utilization', 'Throughput',
              'Average Turnaround Time', 'Average Waiting Time', 'Average Response Time']
values = [cpu_execution_time, cpu_idle_time, cpu_utilization, throughput,
          average_turnaround_time, average_waiting_time, average_response_time]

plt.bar(categories, values)
plt.ylabel('Time or Percentage')  # You can adjust the label based on your data
for i, value in enumerate(values):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
plt.title('Performance Metrics')
plt.show()
