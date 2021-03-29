import os
import csv

def merge_csv_files(folder_path, output_file):
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the folder.")
        return
    
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        
        header_written = False
        
        for file_name in csv_files:
            with open(os.path.join(folder_path, file_name), 'r') as input_csv:
                reader = csv.reader(input_csv)
                header = next(reader)  # Skip header of each file
                
                if not header_written:
                    writer.writerow(header)  # Write header once
                    header_written = True
                
                for row in reader:
                    writer.writerow(row)
    
    print(f"All CSV files merged into {output_file}")

folder_path = input("Enter the folder path containing CSV files: ")
output_file = input("Enter the name of the output merged CSV file: ")
merge_csv_files(folder_path, output_file)
