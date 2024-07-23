import psutil

def display_processes():
    process_list = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    return process_list

def kill_process(process_name):
    for p in psutil.process_iter(['pid', 'name', 'username']):
        if p.info['name'] == process_name:
            p.kill()

def main():
    processes_before = display_processes()
    print("System processes before killing:")
    for process in processes_before:
        print(f"PID: {process['pid']}, Name: {process['name']}, User: {process['username']}")

    name = input("Enter the name of the process to kill: ")
    kill_process(name)

    processes_after = display_processes()
    print("\nSystem processes after killing:")
    for process in processes_after:
        print(f"PID: {process['pid']}, Name: {process['name']}, User: {process['username']}")

if __name__ == "__main__":
    main()

