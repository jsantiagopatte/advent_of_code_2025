import os

if __name__ == "__main__":
    folder_name = "example_files"
    file_name = "practice.txt"
    current_dir = os.getcwd()

    # Import file
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')