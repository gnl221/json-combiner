import os
import json
import datetime
import argparse

def combine_json_files(folder_path):
    # Initialize variables to store the main label and combined data
    main_label = None
    combined_data = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json") and not file_name.startswith("combined"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                data = json.load(file)
                
                # If main_label is not determined yet, get it from the first file
                if main_label is None:
                    main_label, = data.keys()
                    combined_data[main_label] = []
                
                for item in data[main_label]:
                    if item not in combined_data[main_label]:
                        combined_data[main_label].append(item)

    # Generating file name with current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file_name = f"combined-{current_time}.json"

    with open(os.path.join(folder_path, output_file_name), 'w') as output_file:
        json.dump(combined_data, output_file, indent=4)

    print(f"Combined JSON file created: {output_file_name}")

def main():
    parser = argparse.ArgumentParser(description="Combine JSON files into one.")
    parser.add_argument("folder", nargs='?', help="Folder containing JSON files")
    args = parser.parse_args()

    folder_path = args.folder
    if not folder_path:
        folder_path = input("Enter the folder path containing JSON files: ")

    combine_json_files(folder_path)

if __name__ == "__main__":
    main()
