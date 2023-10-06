import multiprocessing
import time


def worker_function(process_label, input_queue, output_queue):
    print(f"Process {process_label} is starting")
    start_time = time.time()

    while time.time() - start_time < 300:  # Run for 5 minutes (300 seconds)
        # Read the value from the input queue
        value = input_queue.get()
        print(f"Process {process_label} received value: {value}")

        # Increment the value
        value += 1

        # Put the updated value into the output queue
        output_queue.put(value)

        # Simulate some work
        time.sleep(2)

    print(f"Process {process_label} is done")


if __name__ == '__main__':
    # Create input and output queues for communication
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    process_labels = ["chandan", "lovnish", "nishit", "vishal"]
    processes = []

    # Initialize the input queue with an initial value
    initial_value = 0
    input_queue.put(initial_value)

    for label in process_labels:
        process = multiprocessing.Process(target=worker_function, args=(label, input_queue, output_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Retrieve the final value from the output queue
    final_value = output_queue.get()

    print(f"All processes are completed. Final value: {final_value}")
