import multiprocessing
import time


def worker_function(x):
    process_name = multiprocessing.current_process().name
    print(f"Worker {process_name} is processing {x}")
    time.sleep(60)  # Sleep for 1 minute
    return x*x


if __name__ == '__main__':
    num_processes = 4  # You can change this number to see more processes in the task manager
    process_names = [f"Process-{i}" for i in range(num_processes)]

    print(f"Starting a Pool with {num_processes} worker processes...")
    with multiprocessing.Pool(num_processes, initializer=multiprocessing.set_start_method('spawn')) as pool:
        results = pool.starmap(worker_function, [(1,), (2,), (3,), (4,)], chunksize=1)

    print("Results:", results)
    print("All worker processes are done.")
