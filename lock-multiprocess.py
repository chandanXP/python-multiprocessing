import multiprocessing
import time


def sender(lock, value):
    while True:
        user_input = input("Enter a number (or 'EXIT' to stop): ")
        if user_input == 'EXIT':
            break

        try:
            value_to_send = int(user_input)
            if value_to_send <= 0:
                print("Value must be greater than 0. Please enter a valid number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        lock.acquire()
        value.value = value_to_send
        lock.release()


def receiver(lock, value):
    while True:
        lock.acquire()
        received_value = value.value
        lock.release()

        if received_value == 'EXIT':
            break

        print(f"Receiver received: {received_value}")


if __name__ == '__main__':
    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    sender_process = multiprocessing.Process(target=sender, args=(lock, shared_value))
    receiver_process = multiprocessing.Process(target=receiver, args=(lock, shared_value))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("Communication complete.")
