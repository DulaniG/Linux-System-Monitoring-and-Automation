import os
import time
from datetime import datetime

LOG_FILE = "submission_log.txt"
SUBMITTED_DIR = "submissions"

failed_attempts = 0
last_attempt_time = 0

# Create directory and log file
os.makedirs(SUBMITTED_DIR, exist_ok=True)
open(LOG_FILE, "a").close()

# Logging function
def log_action(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] - {message}\n")

# Submit assignment
def submit_assignment():
    filename = input("Enter file name: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    # Validate file type
    if not (filename.endswith(".pdf") or filename.endswith(".docx")):
        print("Invalid file format!")
        log_action(f"{filename} rejected (invalid format)")
        return

    # Validate file size (5MB)
    size = os.path.getsize(filename)
    if size > 5 * 1024 * 1024:
        print("File too large!")
        log_action(f"{filename} rejected (too large)")
        return

    destination = os.path.join(SUBMITTED_DIR, filename)

    # Duplicate check (name + content)
    if os.path.exists(destination):
        if open(filename, "rb").read() == open(destination, "rb").read():
            print("Duplicate submission detected!")
            log_action(f"{filename} duplicate rejected")
            return

    # Save file
    with open(filename, "rb") as src, open(destination, "wb") as dst:
        dst.write(src.read())

    print("Submission successful.")
    log_action(f"{filename} submitted successfully")

# Check file submitted
def check_submission():
    filename = input("Enter file name to check: ")
    if os.path.exists(os.path.join(SUBMITTED_DIR, filename)):
        print("File already submitted.")
    else:
        print("File not found.")

# List submissions
def list_submissions():
    files = os.listdir(SUBMITTED_DIR)
    if not files:
        print("No submissions yet.")
    else:
        for f in files:
            print(f)

# Login simulation
def login():
    global failed_attempts, last_attempt_time

    username = input("Enter username: ")
    password = input("Enter password: ")

    current_time = time.time()

    # Detect repeated attempts within 60 seconds
    if current_time - last_attempt_time < 60:
        print("Warning: Multiple login attempts detected!")
        log_action(f"{username} suspicious activity detected")

    last_attempt_time = current_time

    # Simple login check
    if username == "Dulani" and password == "admin123":
        print("Login successful.")
        failed_attempts = 0
        log_action(f"{username} login success")
    else:
        failed_attempts += 1
        print("Login failed.")
        log_action(f"{username} login failed")

        if failed_attempts >= 3:
            print("Account locked due to multiple failed attempts!")
            log_action(f"{username} account locked")

# Exit
def exit_system():
    confirm = input("Are you sure you want to exit? (Y/N): ")
    if confirm.lower() == "y":
        print("Exiting system...")
        exit()
    else:
        print("Cancelled.")

# Menu
while True:
    print("\n===== Secure Submission System =====")
    print("1. Submit Assignment")
    print("2. Check Submission")
    print("3. List Submissions")
    print("4. Login Simulation")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        submit_assignment()
    elif choice == "2":
        check_submission()
    elif choice == "3":
        list_submissions()
    elif choice == "4":
        login()
    elif choice == "5":
        exit_system()
    else:
        print("Invalid option!")
