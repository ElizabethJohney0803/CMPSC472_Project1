import process_creation
import process_management
import thread_support
import ipc
import synchronization
import user_interface
import process_logging

def ipc_operations():
    queue = Queue()
    process = Process(target=ipc.ipc_process, args=(queue,))
    process.start()
    process.join()

    data_received = queue.get()
    print("Received data:", data_received)

def synchronization_operations():
    thread1 = threading.Thread(target=synchronization.synchronized_function)
    thread2 = threading.Thread(target=synchronization.synchronized_function)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


def main():
    while True:
        print("Advanced Process Manager")
        print("1. Create Process")
        print("2. List Processes")
        print("3. Terminate Process")
        print("4. Create Thread")
        print("5. IPC Operations")
        print("6. Synchronization")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            command = input("Enter the command for the process: ")
            process_creation.create_process(command)
        elif choice == "2":
            process_management.list_processes()
        elif choice == "3":
            pid = input("Enter the PID to terminate: ")
            process_management.terminate_process(int(pid))
        elif choice == "4":
            thread_support.create_thread(thread_support.example_thread_function)
        elif choice == "5":
            # Implement IPC operations
            ipc_operations()
            
        elif choice == "6":
            # Implement synchronization operations
            synchronization_operations()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
