import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/faria/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_moved(self,event):
        print(f"Someone has moved or renamed {event.src_path}!")

    def on_modified(self,event):
        print(f"Someone has modified {self.src_path}")

event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()