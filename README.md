# AdvancedOS_1
Setting up Git

#Advanced Operating Systems Assignment

This project contains three tasks implemented using Bash and Python to demonstrate operating system management, scheduling, and security concepts.

___


## Project Structure

AdvancedOS_1/
- Task_01/
    -system_monitor.sh

- Task_02/
    -job_scheduler.py

- Task_03/
    -submission_system.py

___


## Requirements

- Ubuntu / Linux environment
- Bash shell
- Python 3 installed

Check Python version:
'''bash
python3 --version

___


## How to Run the Programs:

#- Task 01 – Process & Resource Management (Bash)

cd Task_01
chmod +x system_monitor.sh
./system_monitor.sh

This script allows:

Viewing CPU and memory usage
Monitoring processes
Managing log files and disk usage

|
|

#- Task 02 – Job Scheduler (Python)

cd Task_02
python3 job_scheduler.py

This program allows:

Submitting jobs
Viewing job queue
Running Round Robin and Priority scheduling
Viewing completed jobs

|
|

#- Task 03 – Secure Submission System (Python)

cd Task_03
python3 submission_system.py

Create test files using:

touch test.pdf
touch test.docx
touch test.txt
fallocate -l 6M large.pdf

This system allows:

Submitting assignments
File validation (.pdf, .docx only)
Duplicate detection
Login simulation with security checks

___


### Features Implemented
Process monitoring and management
Scheduling algorithms (Round Robin & Priority)
File validation and duplicate detection
Logging systems with timestamps
Access control and security monitoring

### Notes
All scripts are menu-driven for easy interaction
Logs are automatically generated for system activities
Designed for educational purposes

___


Author

Student Name: Dulani Gelanigamage
Course: Advanced Operating Systems
Student ID: 100181114
