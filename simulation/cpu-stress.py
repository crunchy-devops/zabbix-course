import time
import random
import threading
import multiprocessing


def cpu_intensive_task(duration):
    """Perform a CPU-intensive task for the given duration."""
    end_time = time.time() + duration
    while time.time() < end_time:
        # Perform more complex CPU-intensive work
        for _ in range(1000000):
            x = 0
            y = 1
            for i in range(1, 100):
                x += i ** 2
                y *= i


def simulate_random_cpu_activity(core_count, multiplier=2):
    """Simulate random CPU activity using multiple threads or processes."""
    while True:
        # Generate a random duration for CPU activity
        activity_duration = random.uniform(5, 10)  # Between 5 and 10 seconds
        # Generate a random sleep duration
        sleep_duration = random.uniform(2, 5)  # Between 2 and 5 seconds

        # Calculate the number of workers to start (more than the number of CPU cores)
        num_workers = core_count * multiplier

        print(f"Starting CPU activity with {num_workers} workers for {activity_duration:.2f} seconds")

        # Create a thread or process for each worker
        workers = []
        for _ in range(num_workers):
            worker = multiprocessing.Process(target=cpu_intensive_task, args=(activity_duration,))
            workers.append(worker)
            worker.start()

        # Wait for all workers to finish
        for worker in workers:
            worker.join()

        print(f"Sleeping for {sleep_duration:.2f} seconds")
        time.sleep(sleep_duration)


if __name__ == "__main__":
    # Get the number of CPU cores
    core_count = multiprocessing.cpu_count()
    print(f"Detected {core_count} CPU cores")

    # Simulate CPU activity
    simulate_random_cpu_activity(core_count)
