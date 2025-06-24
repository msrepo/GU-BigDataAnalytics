import os
import glob

def find_task_a_files(data_folder):
    """
    Find all files in the specified folder that are related to Task A (ending with _taska.txt).
    """
    # Use glob to find files ending with '_taska.txt'
    task_a_files = glob.glob(os.path.join(data_folder, "*_taska.txt"))
    return task_a_files

def read_file_content(file_path):
    """
    Read the content of a file and return it. The encoding may vary from us-ascii, to utf-8 to unknown-8bit
    """
    with open(file_path, 'rb') as file:
        content = file.read()
    try:
        # Try decoding with utf-8 first
        return content.decode('utf-8')
    except UnicodeDecodeError:
        try:
            # If utf-8 fails, try decoding with us-ascii
            return content.decode('us-ascii')
        except UnicodeDecodeError:
            # If both fail, return the raw bytes as a string
            return content.decode('latin-1', errors='ignore')
        
def save_dict_to_json(data, file_path):
    """
    Save a dictionary to a JSON file.
    """
    import json
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        
def main():
    # Specify the folder containing the data files
    data_folder = "data"  # Replace with the path to your data folder

    # Find Task A files
    task_a_files = find_task_a_files(data_folder)

    # Print the results
    if task_a_files:
        print("Files related to Task A:")
        for file in task_a_files:
            print(file)
    else:
        print("No files related to Task A found.")
    
    # read these files with each content
    task_a_subsets = {} 
    for file in task_a_files:
        content = read_file_content(file)
        # extract the subset name from the file name
        subset_name = os.path.basename(file).replace("_taska.txt", "")
        task_a_subsets[subset_name] = content
    
    #save to json
    output_file = os.path.join(data_folder, "task_a_subsets.json")
    save_dict_to_json(task_a_subsets, output_file) 

if __name__ == "__main__":
    main()