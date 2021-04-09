import os
import time

def watch_files(directory):
    files = {f: os.path.getmtime(f) for f in os.listdir(directory)}
    while True:
        for f in os.listdir(directory):
            mtime = os.path.getmtime(f)
            if mtime != files.get(f, None):
                print(f"File {f} has been modified.")
                files[f] = mtime
        time.sleep(1)

directory = "C:/path/to/your/folder"
watch_files(directory)
