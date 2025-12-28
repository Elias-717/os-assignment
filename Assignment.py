import time

# Define process states
NEW = "New"
READY = "Ready"
RUNNING = "Running"
WAITING = "Waiting"
TERMINATED = "Terminated"

# Process class
class Process:
    def __init__(self, pid, burst_time, io_required=False):
        self.pid = pid
        self.burst_time = burst_time
        self.io_required = io_required
        self.state = NEW

    def __str__(self):
        return f"{self.pid}: {self.state}"

# Create processes
processes = [
    Process("P1", 3, io_required=True),
    Process("P2", 2),
    Process("P3", 2, io_required=True)
]

ready_queue = []

print("=== OS Process Lifecycle Simulation (FCFS) ===\n")

# Move processes to Ready state
for p in processes:
    p.state = READY
    ready_queue.append(p)
    print(f"{p.pid} moved to READY")

print("\n--- CPU Scheduling Start ---\n")

# FCFS Scheduling
while ready_queue:
    current = ready_queue.pop(0)
    current.state = RUNNING
    print(f"{current.pid} is RUNNING")

    # Simulate CPU execution
    time.sleep(1)

    # Simulate I/O if required
    if current.io_required:
        current.state = WAITING
        print(f"{current.pid} is WAITING (I/O)")
        time.sleep(1)
        current.state = READY
        print(f"{current.pid} returned to READY")
        current.io_required = False
        ready_queue.append(current)
    else:
        current.state = TERMINATED
        print(f"{current.pid} is TERMINATED")

    print()

print("=== Simulation Complete ===")
