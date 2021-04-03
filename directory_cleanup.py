import os
import time

def cleanup_old_files(folder_path, days):
    current_time = time.time()
    cutoff_time = current_time - (days * 86400)  # 86400 seconds in a day
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            last_modified = os.path.getmtime(file_path)
            if last_modified < cutoff_time:
                os.remove(file_path)
                print(f"Deleted: {file_name}")

folder_path = input("Enter the folder path to clean: ")
days = int(input("Enter the number of days to keep files: "))
cleanup_old_files(folder_path, days)
print("Cleanup complete!")
