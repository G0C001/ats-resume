import os

def collect_and_rename_pdfs(new_name_prefix):
    folder_path = './templates'
    for index, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.pdf'):
            new_filename = new_name_prefix
            
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")