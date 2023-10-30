Project Report: Advanced Process Manager with Process Synchronization
Title

Advanced Process Manager with Process Synchronization
Implemented Functionalities

    Process Creation: Users can create new processes using system calls (e.g., subprocess).
    Process Management: Functionalities to list, terminate, and monitor running processes using the psutil library.
    Thread Support: Support for multiple threads within a process using the threading module.
    Inter-Process Communication (IPC): IPC mechanisms implemented with Python's multiprocessing for message passing.
    Process Synchronization: Synchronization mechanisms using thread locking with threading.
    Command-Line Interface (CLI): User-friendly interface for interacting with the Process Manager.
    Logging and Reporting: Logging significant events and information using the logging module.

Installation

    Run the main application script with python main.py.

Usage

    Execute main.py to start the Process Manager.
    Choose options from the command-line interface to create processes, list processes, terminate processes, create threads, and perform IPC and synchronization operations.
    Follow the prompts and input commands or data as requested.

Test Results
Functionality: Process Creation

    Test Case 1: Creating a simple process.
        Input: notepad.exe
        Output: Process ID (PID) of the newly created Notepad process.
        Explanation: The command successfully started the Notepad process.

Functionality: Process Management

    Test Case 1: Listing running processes.
        Output: List of processes with their PID, name, and status.
        Explanation: The Process Manager correctly listed all running processes.
    Test Case 2: Terminating a process.
        Input: Process PID
        Output: Confirmation message
        Explanation: The specified process was terminated successfully.

Functionality: Thread Support

    Test Case 1: Creating and running a thread.
        Output: "Thread running" (printed twice).
        Explanation: Two threads were created and executed concurrently.

Functionality: Inter-Process Communication (IPC)

    Test Case 1: Sending data between processes.
        Output: "Received data: Hello from the IPC process!"
        Explanation: Data was successfully passed between processes.

Functionality: Process Synchronization

    Test Case 1: Synchronized function.
        Output: "Synchronized function running" (printed twice).
        Explanation: The synchronized function executed in a mutually exclusive manner due to locking.

Discussion

The Advanced Process Manager with Process Synchronization project successfully implemented the specified functionalities. The system demonstrated the ability to create and manage processes, create and synchronize threads, and facilitate inter-process communication. Key features such as process listing and termination, thread support, IPC, and synchronization were validated through test cases.

The project can be further extended by implementing advanced IPC mechanisms, additional synchronization primitives, and enhanced logging and reporting features. Overall, the project serves as a foundation for a robust and flexible Process Manager that can be used in various computing environments.

Conclusion

The project report summarizes the design, implementation, and testing of the Advanced Process Manager with Process Synchronization. The functionalities provided cater to process creation, management, thread support, IPC, synchronization, and a user-friendly interface. The system's successful execution of test cases demonstrates its functionality and reliability.

