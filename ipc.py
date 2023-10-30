"""import multiprocessing

def worker_function(data):
    print(f"Received data: {data}")

if __name__ == '__main__':
    data_to_send = "Hello!"
    process = multiprocessing.Process(target=worker_function, args=(data_to_send,))
    process.start()"""


from multiprocessing import Process, Queue

def ipc_process(queue):
    # This function will be executed in a separate process
    data_to_send = "IPC process!"
    queue.put(data_to_send)