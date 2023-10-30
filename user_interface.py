import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Process Manager")
    parser.add_argument("--create", help="Create a new process")
    parser.add_argument("--list", help="List running processes")
    parser.add_argument("--terminate", help="Terminate a process")

    args = parser.parse_args()

    if args.create:
        create_process(args.create)
    elif args.list:
        list_processes()
    elif args.terminate:
        terminate_process(int(args.terminate))

if __name__ == "__main__":
    main()
