import subprocess

def create_process(command):
    try:
        subprocess.Popen(command, shell=True)
        print("Process started successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
#create_process("notepad.exe")
