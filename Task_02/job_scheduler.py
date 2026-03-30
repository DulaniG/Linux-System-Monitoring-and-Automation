import time
from datetime import datetime

QUEUE_FILE = "job_queue.txt"
COMPLETED_FILE = "completed_jobs.txt"
LOG_FILE = "scheduler_log.txt"

# Create files if not exist
open(QUEUE_FILE, 'a').close()
open(COMPLETED_FILE, 'a').close()
open(LOG_FILE, 'a').close()

# Logging function
def log_action(student_id, job_name, action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] - {student_id} - {job_name} - {action}\n")

# Submit job
def submit_job():
    student_id = input("Enter Student ID: ")
    job_name = input("Enter Job Name: ")
    time_needed = int(input("Enter execution time (seconds): "))
    priority = int(input("Enter priority (1-10): "))

    if priority < 1 or priority > 10:
        print("Invalid priority!")
        return

    with open(QUEUE_FILE, "a") as f:
        f.write(f"{student_id},{job_name},{time_needed},{priority}\n")

    log_action(student_id, job_name, "Job Submitted")
    print("Job added successfully.")

# View queue
def view_jobs():
    with open(QUEUE_FILE, "r") as f:
        jobs = f.readlines()

    if not jobs:
        print("No pending jobs.")
    else:
        print("Pending Jobs:")
        for job in jobs:
            print(job.strip())

# View completed jobs
def view_completed():
    with open(COMPLETED_FILE, "r") as f:
        jobs = f.readlines()

    if not jobs:
        print("No completed jobs.")
    else:
        print("Completed Jobs:")
        for job in jobs:
            print(job.strip())

# Round Robin Scheduling
def round_robin():
    quantum = 5
    with open(QUEUE_FILE, "r") as f:
        jobs = [line.strip().split(",") for line in f.readlines()]

    if not jobs:
        print("No jobs to process.")
        return

    print("Processing using Round Robin...")

    while jobs:
        for job in jobs[:]:
            student_id, job_name, time_needed, priority = job
            time_needed = int(time_needed)

            if time_needed > quantum:
                print(f"Running {job_name} for {quantum} for 5s")
                time.sleep(5)
                job[2] = str(time_needed - quantum)
            else:
                print(f"Completing {job_name}")
                time.sleep(1)

                with open(COMPLETED_FILE, "a") as f:
                    f.write(",".join(job) + "\n")

                log_action(student_id, job_name, "Round Robin Completed")
                jobs.remove(job)

    open(QUEUE_FILE, "w").close()

# Priority Scheduling
def priority_scheduling():
    with open(QUEUE_FILE, "r") as f:
        jobs = [line.strip().split(",") for line in f.readlines()]

    if not jobs:
        print("No jobs to process.")
        return

    jobs.sort(key=lambda x: int(x[3]), reverse=True)

    print("Processing using Priority Scheduling...")

    for job in jobs:
        student_id, job_name, time_needed, priority = job

        print(f"Running {job_name} (Priority {priority})")
        time.sleep(1)

        with open(COMPLETED_FILE, "a") as f:
            f.write(",".join(job) + "\n")

        log_action(student_id, job_name, "Priority Completed")

    open(QUEUE_FILE, "w").close()

# Exit
def exit_system():
    confirm = input("Are you sure you want to exit? (Y/N): ")
    if confirm.lower() == "y":
        print("Exiting system...Bye")
        exit()
    else:
        print("Cancelled.")

# Menu
while True:
    print("\n===== Job Scheduler Menu =====")
    print("1. Submit Job")
    print("2. View Pending Jobs")
    print("3. Process Jobs (Round Robin)")
    print("4. Process Jobs (Priority)")
    print("5. View Completed Jobs")
    print("6. Exit (Bye)")

    choice = input("Enter choice: ")

    if choice == "1":
        submit_job()
    elif choice == "2":
        view_jobs()
    elif choice == "3":
        round_robin()
    elif choice == "4":
        priority_scheduling()
    elif choice == "5":
        view_completed()
    elif choice == "6":
        exit_system()
    else:
        print("Invalid choice!")
