import os
import time
import random
import threading


def write_file(file_path, size_mb):
    """Write a file of the specified size in MB."""
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_mb * 1024 * 1024))


def read_file(file_path):
    """Read the file."""
    with open(file_path, 'rb') as f:
        while f.read(1024 * 1024):
            pass


def get_disk_usage_percentage(directory):
    """Get the disk usage percentage of the specified directory."""
    st = os.statvfs(directory)
    total_blocks = st.f_blocks
    free_blocks = st.f_bfree
    used_blocks = total_blocks - free_blocks
    usage_percentage = (used_blocks / total_blocks) * 100
    return usage_percentage


def fill_disk_to_target(directory, target_usage, file_size_mb):
    """Fill the disk until the target usage percentage is reached."""
    while get_disk_usage_percentage(directory) < target_usage:
        file_path = os.path.join(directory, f'test_file_{random.randint(1000, 9999)}.bin')
        write_file(file_path, file_size_mb)


def stress_test_disk(directory, duration):
    """Perform disk stress test with multiple threads."""
    end_time = time.time() + duration
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith('test_file_')]

    while time.time() < end_time:
        threads = []
        for file_path in files:
            t_write = threading.Thread(target=write_file, args=(file_path, 1))
            t_read = threading.Thread(target=read_file, args=(file_path,))
            threads.append(t_write)
            threads.append(t_read)
            t_write.start()
            t_read.start()

        for t in threads:
            t.join()

        time.sleep(0.1)


def clean_up(directory):
    """Remove all test files."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.startswith('test_file_')]
    for file_path in files:
        os.remove(file_path)


if __name__ == "__main__":
    directory = "/home/ubuntu/test"  # Specify the directory to perform the stress test
    target_usage = 85  # Target disk usage percentage
    file_size_mb = 100  # Size of each test file in MB
    duration = 600  # Duration of the stress test in seconds (e.g., 10 minutes)

    print(f"Starting disk fill to reach {target_usage}% usage")
    fill_disk_to_target(directory, target_usage, file_size_mb)
    print(f"Disk filled to {target_usage}% usage. Starting stress test for {duration} seconds")
    stress_test_disk(directory, duration)
    print("Cleaning up test files")
    clean_up(directory)
    print("Disk stress test completed")
