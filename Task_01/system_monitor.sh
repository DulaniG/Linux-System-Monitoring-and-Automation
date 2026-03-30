#! /bin/bash

LOG_FILE="system_monitor_log.txt"

# Create log file if not exists
touch $LOG_FILE

# Logging function
log_action() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] - $1" >> $LOG_FILE
}

# Show CPU & Memory
show_usage() {
    echo "----- CPU and Memory Usage -----"
    top -b -n1 | head -12
    log_action "Checked CPU and memory usage"
}

# Show top processes
show_processes() {
    echo "----- Top 10 Memory Processes -----"
    ps -eo pid,user,%cpu,%mem --sort=-%mem | head -11
    log_action "Viewed top processes"
}

# Kill process safely
kill_process() {
    read -p "Enter PID to terminate: " pid

    if ! [[ "$pid" =~ ^[0-9]+$ ]]; then
        echo "Invalid PID!"
        log_action "Invalid PID entered"
        return
    fi

    if [ "$pid" -eq 1 ]; then
        echo "Cannot terminate critical system process!"
        log_action "Attempt to kill critical process PID 1"
        return
    fi

    read -p "Are you sure you want to kill process $pid? (Y/N): " confirm

    if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
        kill $pid 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "Process terminated."
            log_action "Process $pid terminated"
        else
            echo "Failed to terminate process."
            log_action "Failed to terminate process $pid"
        fi
    else
        echo "Cancelled."
        log_action "Cancelled termination of PID $pid"
    fi
}

# Disk usage
check_disk_usage() {
    read -p "Enter directory path: " dir

    if [ -d "$dir" ]; then
        du -sh "$dir"
        log_action "Checked disk usage of $dir"
    else
        echo "Directory not found!"
        log_action "Invalid directory entered: $dir"
    fi
}

# Find large logs
find_large_logs() {
    echo "----- Large Log Files (>50MB) -----"
    files=$(find . -type f -name "*.log" -size +50M)

    if [ -z "$files" ]; then
        echo "No large log files found."
        log_action "No large log files found"
    else
        echo "$files"
        log_action "Displayed large log files"
    fi
}

# Archive logs
archive_logs() {

    if [ ! -d "ArchiveLogs" ]; then
        mkdir ArchiveLogs
        echo "ArchiveLogs directory created."
        log_action "Created ArchiveLogs directory"
    fi

    files=$(find . -type f -name "*.log" -size +50M)

    if [ -z "$files" ]; then
        echo "No large log files to archive."
        log_action "No files to archive"
    else
        for file in $files
        do
            filename=$(basename "$file")
            timestamp=$(date +%Y%m%d%H%M%S)
            gzip -c "$file" > "ArchiveLogs/${filename}_$timestamp.gz"
            echo "Archived: $file"
            log_action "Archived file $file"
        done
    fi

    size=$(du -sm ArchiveLogs | cut -f1)

    if [ "$size" -gt 1024 ]; then
        echo "WARNING: ArchiveLogs exceeds 1GB!"
        log_action "ArchiveLogs exceeded 1GB"
    fi
}

# Exit function (Bye command)
exit_system() {
    read -p "Are you sure you want to exit? (Y/N): " confirm

    if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
        echo "Exiting system...Bye"
        log_action "User exited the system"
        exit 0
    else
        echo "Exit cancelled."
        log_action "User cancelled exit"
    fi
}

# MENU
while true
do
    echo ""
    echo "===== System Monitor Menu ====="
    echo "1. Show CPU & Memory Usage"
    echo "2. Show Top Processes"
    echo "3. Kill a Process"
    echo "4. Check Disk Usage"
    echo "5. Find Large Log Files"
    echo "6. Archive Log Files"
    echo "7. Exit (Bye)"

    read -p "Enter choice: " choice

    case $choice in
        1) show_usage ;;
        2) show_processes ;;
        3) kill_process ;;
        4) check_disk_usage ;;
        5) find_large_logs ;;
        6) archive_logs ;;
        7) exit_system ;;
        *) echo "Invalid option!" ;;
    esac
done
