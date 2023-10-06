import multiprocessing
import time


def sender(input_queue, output_queue):
    value = 1

    while value <= 1024:
        input_queue.put(value)
        print(f"Sender sent: {value}")

        # Receive the processed value from the receiver
        doubled_value = output_queue.get()
        print(f"Sender received: {doubled_value}")

        value = doubled_value
        time.sleep(2)  # Introduce a 2-second delay


def receiver(input_queue, output_queue):
    while True:
        value = input_queue.get()
        print(f"Receiver received: {value}")

        if value > 1024:
            break

        doubled_value = value * 2
        time.sleep(2)  # Introduce a 2-second delay

        # Send the doubled value back to the sender
        output_queue.put(doubled_value)


if __name__ == '__main__':
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    sender_process = multiprocessing.Process(target=sender, args=(input_queue, output_queue))
    receiver_process = multiprocessing.Process(target=receiver, args=(input_queue, output_queue))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("Communication complete.")
