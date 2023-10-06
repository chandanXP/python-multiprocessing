import multiprocessing
import time


def worker_function():
    print(f"Worker {multiprocessing.current_process().name} is working")
    time.sleep(60)  # Sleep for 1 minute


if __name__ == '__main__':
    num_processes = 4  # You can change this number to see more processes in the task manager
    processes = []

    print(f"Starting {num_processes} worker processes...")
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_function)
        processes.append(process)
        process.start()

    print("Waiting for processes to finish...")
    time.sleep(300)  # Wait for 5 minutes

    print("Terminating processes...")
    for process in processes:
        process.terminate()

    print("All processes terminated.")
