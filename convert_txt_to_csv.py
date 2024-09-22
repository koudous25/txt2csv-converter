import csv
import os

# Function to read the .txt file and convert it to .csv


def convert_txt_to_csv(input_folder, output_folder, txt_filename, csv_filename):
    # Ensure input and output directories exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Full paths to the input and output files
    txt_file = os.path.join(input_folder, txt_filename)
    csv_file = os.path.join(output_folder, csv_filename)

    with open(txt_file, 'r', encoding='utf-8') as txt_f:
        lines = txt_f.readlines()

    # Open the .csv file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_f:
        writer = csv.writer(csv_f)

        for line in lines:
            # Remove quotes, split columns by tab characters
            row = line.replace('"', '').strip().split('\t')
            writer.writerow(row)


# Define the folders and filenames
input_folder = 'input'
output_folder = 'output'
txt_filename = 'fruits_vegetables_data.txt'
csv_filename = 'fruits_vegetables_data.csv'

# Conversion
convert_txt_to_csv(input_folder, output_folder, txt_filename, csv_filename)

print(
    f"Conversion complete. CSV file saved as {csv_filename} in the {output_folder} folder.")
