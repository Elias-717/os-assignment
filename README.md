# Assignment.py - OS Process Lifecycle Simulation (FCFS Scheduling)

## 📋 Overview

This Python program simulates an **Operating System (OS) process lifecycle** using the **First-Come-First-Served (FCFS)** CPU scheduling algorithm. It demonstrates how processes transition through different states as they compete for CPU time.

---

## 🎯 What Does This Code Do?

The program:
1. Creates multiple processes with different CPU burst times
2. Places all processes in the READY queue
3. Schedules processes using FCFS algorithm
4. Simulates I/O operations for some processes
5. Shows state transitions from creation to termination

---

## 🏗️ Architecture & Components

### 1. **Process States**

```
States Defined:
├── NEW → process created
├── READY → waiting to run
├── RUNNING → executing on CPU
├── WAITING → blocked by I/O
└── TERMINATED → completed
```

### 2. **Process Class**

```python
class Process:
    pid              # Process ID (P1, P2, P3)
    burst_time       # CPU time needed
    io_required      # I/O dependency flag
    state            # Current state
```

---

## 📊 Execution Flow (State Diagram)
The following diagram is an illustration of the whole process.

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESS LIFECYCLE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────┐      ┌───────┐      ┌─────────┐                       │
│  │ NEW  │─────→│ READY │─────→│ RUNNING │                       │
│  └──────┘      └───────┘      └─────────┘                       │
│                    ▲              │                              │
│                    │              │                              │
│                    │         ┌────┴──────────────┐               │
│                    │         │                   ▼               │
│                    │      (if I/O)           ┌─────────┐         │
│                    │         │               │ WAITING │         │
│                    │         │               └────┬────┘         │
│                    │         │                    │               │
│                    └────────────────────────────┐ │               │
│                                   (if no I/O)  │ ▼               │
│                                            ┌──────────────┐      │
│                                            │ TERMINATED   │      │
│                                            └──────────────┘      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 FCFS (First-Come-First-Served) Scheduling Algorithm

```
FCFS Queue Operations:

READY QUEUE:
    append(P1)  append(P2)  append(P3)
    
    ┌─────────────────────────────┐
    │  P1  │  P2  │  P3           │
    └─────────────────────────────┘
      ▲                        ▲
    append()                 pop(0)
    (back)                   (front)
    
Execution Order: P1 → P2 → P3 (FIFO - queue order) The order starts from p1 and ends at p3
```

---

## 🎬 Simulation Timeline

### **Input Data:**

| Process | Burst Time | I/O Required |
|---------|-----------|--------------|
| P1      | 3 sec     | Yes ✓        |
| P2      | 2 sec     | No ✗         |
| P3      | 2 sec     | Yes ✓        |

### **Execution Timeline:**

```
Time    Event                          State
────────────────────────────────────────────────
 0s     P1, P2, P3 → READY            [Ready Queue: P1→P2→P3]
 0s     P1 starts execution           [P1: RUNNING]
 1s     P1 needs I/O                  [P1: WAITING]
 2s     P1 I/O done, back to queue    [P1: READY, Queued]
 2s     P2 starts execution           [P2: RUNNING]
 3s     P2 completes                  [P2: TERMINATED]
 3s     P3 starts execution           [P3: RUNNING]
 4s     P3 needs I/O                  [P3: WAITING]
 5s     P3 I/O done                   [P3: READY, Queued]
 5s     P1 resumes execution          [P1: RUNNING]
 6s     P1 completes                  [P1: TERMINATED]
 6s     P3 resumes execution          [P3: RUNNING]
 7s     P3 completes                  [P3: TERMINATED]
 7s     ✓ SIMULATION COMPLETE
```

---

## 💻 Code Breakdown

### **Section 1: Initialization**

```python
for p in processes:
    p.state = READY                 # Change state
    ready_queue.append(p)           # Add to queue
    print(f"{p.pid} moved to READY")
```

**Visual:**
```
Processes List          Ready Queue
├─ P1 (state=NEW)  ─→  ├─ P1 (state=READY)
├─ P2 (state=NEW)  ─→  ├─ P2 (state=READY)
└─ P3 (state=NEW)  ─→  └─ P3 (state=READY)
```

### **Section 2: FCFS Scheduling Loop**

```python
while ready_queue:
    current = ready_queue.pop(0)        # Get first process
    current.state = RUNNING             # Execute
    time.sleep(1)                       # Simulate 1 sec CPU time
```

**Visual:**
```
Iteration 1:
Ready Queue: [P1, P2, P3]
pop(0) ──→ current = P1
Ready Queue: [P2, P3]

Iteration 2:
Ready Queue: [P2, P3]
pop(0) ──→ current = P2
Ready Queue: [P3]

...and so on
```

### **Section 3: I/O Simulation**

```python
if current.io_required:
    current.state = WAITING             # Block process
    time.sleep(1)                       # Simulate I/O time
    current.state = READY               # Unblock
    ready_queue.append(current)         # Re-queue
    current.io_required = False         # Mark done
else:
    current.state = TERMINATED          # Complete
```

**Visual:**
```
Process with I/O:              Process without I/O:

P1 (io_required=True)         P2 (io_required=False)
  │                              │
  ├─ RUNNING (1 sec)            ├─ RUNNING (1 sec)
  │                              │
  ├─ WAITING (1 sec) [I/O]       └─ TERMINATED ✓
  │
  ├─ READY (re-queued)
  │
  └─ RUNNING (again)
     │
     └─ TERMINATED ✓
```

---

## 📈 Key Concepts Illustrated

| Concept | What Happens | Why It Matters |
|---------|--------------|----------------|
| **Context Switching** | P1 (RUNNING) → P2 (RUNNING) | OS must manage CPU time fairly |
| **I/O Blocking** | P1 enters WAITING state | Prevents CPU from sitting idle |
| **Queue Order** | FCFS uses `pop(0)` | Simple but not always efficient |
| **State Transitions** | NEW → READY → RUNNING → TERMINATED | Shows full process lifecycle |
| **Re-queuing** | I/O process returns to READY | Allows processes to resume fairly |

---

## ⚡ Performance Characteristics (FCFS)

### Advantages ✓
- **Simple to implement** - Just use a queue
- **Fair** - All processes get CPU time
- **No starvation** - Processes will eventually run

### Disadvantages ✗
- **Not optimal** - Long processes block short ones
- **Average wait time** can be high
- **Poor for interactive systems** - Users experience delays

**Example Problem:**
```
If P1 takes 100 sec and P2 takes 1 sec:
  P1 runs → P2 waits 100 sec (poor experience!)
  
Better: SRTF (Shortest Remaining Time First) would run P2 first
```

---

## 🚀 How to Run

```bash
python Assignment.py
```

**Expected Output:**
```
=== OS Process Lifecycle Simulation (FCFS) ===

P1 moved to READY
P2 moved to READY
P3 moved to READY

--- CPU Scheduling Start ---

P1 is RUNNING
P1 is WAITING (I/O)
P1 returned to READY

P2 is RUNNING
P2 is TERMINATED

P3 is RUNNING
P3 is WAITING (I/O)
P3 returned to READY

P1 is RUNNING
P1 is TERMINATED

P3 is RUNNING
P3 is TERMINATED

=== Simulation Complete ===
```

---

## 🔧 Customization Ideas

### **Add More Processes:**
```python
processes = [
    Process("P1", 3, io_required=True),
    Process("P2", 2),
    Process("P3", 2, io_required=True),
    Process("P4", 1),  # New process
    Process("P5", 4, io_required=True),  # New process
]
```

### **Change Burst Time:**
```python
Process("P1", 5)  # Increase to 5 seconds
```

### **Disable I/O:**
```python
Process("P1", 3, io_required=False)  # No I/O blocking
```

### **Faster Simulation:**
```python
time.sleep(0.5)  # Use 0.5 seconds instead of 1
```

---

## 📚 Learning Outcomes

After studying this code, you'll understand:

✅ **Process States** - How processes move between states  
✅ **Queue Data Structure** - FIFO behavior with `pop(0)`  
✅ **CPU Scheduling** - FCFS algorithm implementation  
✅ **I/O Operations** - How blocking and unblocking work  
✅ **State Machines** - Transitions and conditions  
✅ **Simulation** - Using `time.sleep()` for realistic timing  

---

## 🎓 Real-World Applications

This simulation models real OS behaviors in:
- **Thread Schedulers** (Java, Python threading)
- **Process Managers** (Linux, Windows Task Manager)
- **Job Queues** (Database engines, web servers)
- **Task Scheduling** (Kubernetes, Docker)

---

## 📝 Notes

- The program uses `time.sleep()` for simulation, so **total runtime is ~7-8 seconds**
- FCFS is used in **real operating systems** but often with **time slicing** (round-robin)
- Modern systems use more **sophisticated algorithms** (Priority Queue, Multilevel Feedback)
- This is an **educational simulation**, not production-grade OS code

---

**Created for:** Learning OS Concepts  
**Difficulty Level:** Beginner → Intermediate  
**Topics:** Operating Systems, Process Scheduling, State Machines
