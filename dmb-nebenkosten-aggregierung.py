import os
import re
import csv

def sum_numbers_in_file(file_path):
    """Reads a file and returns the sum of all numbers in it."""
    total_sum = 0
    with open(file_path, 'r') as file:
        content = file.read()
        # Replace commas with dots for decimal numbers and find all numbers
        content = content.replace(',', '.')
        # Find all numbers (including integers and decimals)
        numbers = re.findall(r'-?\d+\.?\d*', content)
        # Sum all the numbers
        total_sum = sum(float(num) for num in numbers)
    return total_sum

def process_files_in_folder(folder_path, output_csv):
    """Processes all .txt files in a folder and writes their sum to a CSV."""
    # Open a CSV file for writing the output
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        # Write the header of the CSV
        writer.writerow(["Jahr", "Summe Nebenkosten"])
        
        # List all .txt files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder_path, file_name)
                total_sum = sum_numbers_in_file(file_path)
                # Write the file name and the sum of numbers to the CSV
                writer.writerow([file_name[:-4], total_sum])
                
    print(f"Results saved in {output_csv}")


folder_path = 'dmb-nebenkosten-raw'  # Replace with the path to your folder
output_csv = 'maximale-nebenkosten.csv'  # Output CSV file

process_files_in_folder(folder_path, output_csv)