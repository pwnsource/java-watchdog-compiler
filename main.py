import subprocess
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JavaFileHandler(FileSystemEventHandler):
    def __init__(self, log_errors=False):
        super().__init__()
        self.log_errors = log_errors
        if self.log_errors:
            self.log_file = open("log.txt", "a")

    def on_modified(self, event):
        if event.is_directory:
            return
        filename, extension = os.path.splitext(event.src_path)
        if extension == '.java':
            print(f"Detected change in {event.src_path}")
            self.compile_java(event.src_path)

    def compile_java(self, file_path):
        print("Compiling...")
        try:
            subprocess.run(['javac', file_path], check=True)
            print("Compilation finished successfully.")
        except subprocess.CalledProcessError as e:
            error_message = f"Error compiling {file_path}: {e}"
            print(error_message)
            if self.log_errors:
                self.log_error(error_message)

    def log_error(self, error_message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.log_file.write(f"[{timestamp}] {error_message}\n")
        self.log_file.flush()

    def __del__(self):
        if self.log_errors:
            self.log_file.close()

def main():
    target_path = input("Enter the full path to the file or folder to monitor: ")
    if os.path.isdir(target_path):
        folder_to_watch = target_path
    elif os.path.isfile(target_path):
        folder_to_watch, _ = os.path.split(target_path)
    else:
        print("Invalid path.")
        return

    log_errors = input("Do you want to log errors? (yes/no): ").lower() == "yes"
    event_handler = JavaFileHandler(log_errors=log_errors)
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
