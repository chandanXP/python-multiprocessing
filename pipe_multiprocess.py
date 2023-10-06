import multiprocessing
import time


def process_with_lock(lock):
    print("Process 1: Acquiring the lock...")
    lock.acquire()
    print("Process 1: Lock acquired. Performing some work...")
    time.sleep(2)  # Simulate some work for 2 seconds
    lock.release()
    print("Process 1: Lock released.")


def process_without_lock(lock):
    print("Process 2: Waiting for the lock...")
    lock.acquire()  # Wait for the lock to be released by Process 1
    print("Process 2: Lock acquired. Performing some work...")
    time.sleep(2)  # Simulate some work for 2 seconds
    lock.release()
    print("Process 2: Lock released.")


if __name__ == '__main__':
    lock = multiprocessing.Lock()

    # Create two processes
    process1 = multiprocessing.Process(target=process_with_lock, args=(lock,))
    process2 = multiprocessing.Process(target=process_without_lock, args=(lock,))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Both processes are completed.")
