import psutil

def list_processes():
    for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
        print(process.info)

def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process {pid} terminated.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
#list_processes()
#terminate_process(1234)  # Replace with a valid PID.
