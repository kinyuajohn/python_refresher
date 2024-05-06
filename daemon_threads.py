print("----------------------------------------------")
# --------------------- daemon threads ---------------------
# ----------------------------------------------------------
# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    print()

    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds.")


x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit? ")
