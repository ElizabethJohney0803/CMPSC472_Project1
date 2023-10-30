import threading

def create_thread(target_function):
    thread = threading.Thread(target=target_function)
    thread.start()

def example_thread_function():
    print("Thread running")

# Example usage:
#create_thread(example_thread_function)
