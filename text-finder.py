import os

def search_in_files(folder_path, keyword):
    found = False
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                lines = file.readlines()
                for line_num, line in enumerate(lines, start=1):
                    if keyword.lower() in line.lower():
                        found = True
                        print(f"Keyword found in {file_name} (Line {line_num}): {line.strip()}")
    
    if not found:
        print(f"No occurrences of '{keyword}' found in the folder.")

folder_path = input("Enter the folder path to search in: ")
keyword = input("Enter the keyword to search for: ")
search_in_files(folder_path, keyword)
