import threading

lock = threading.Lock()

def synchronized_function():
    with lock:
        print("Synchronized function running")

# Example usage:
#thread1 = threading.Thread(target=synchronized_function)
#thread2 = threading.Thread(target=synchronized_function)
#thread1.start()
#thread2.start()
