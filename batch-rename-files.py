import os

def batch_rename_files(directory, prefix):
    files = os.listdir(directory)
    for index, file in enumerate(files):
        old_file = os.path.join(directory, file)
        if os.path.isfile(old_file):
            file_extension = os.path.splitext(file)[1]
            new_name = f"{prefix}_{index+1}{file_extension}"
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed {file} to {new_name}")

# Example Usage
directory = r"C:\path\to\your\folder"
batch_rename_files(directory, "image")
