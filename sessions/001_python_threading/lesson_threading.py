"""Session work for TOPIC."""
import threading
import time



def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")



threading.Thread(target=worker, daemon=True, args=("ABC",)).start()
threading.Thread(target=worker, daemon=True, args=("XYZ",)).start()

input("Press enter to quit \n")


