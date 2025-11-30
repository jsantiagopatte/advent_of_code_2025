import os
import numpy as np

if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "practice.txt"
    current_dir = os.getcwd()

    # Import file
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')

    # Store max and current value.
    current_cal = 0
    max_cal = 0
    # Run trough list.
    for line in file:
        line_clean = line.strip()
        if line_clean.isnumeric():
            current_cal += float(line_clean)
        else:
            if current_cal > max_cal:
                max_cal = current_cal
            current_cal = 0
    
    print(f"Part 1: {max_cal}")

    # Part 2:
    current_cal = 0
    elves_list = []
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    for line in file:
        line_clean = line.strip()
        if line_clean.isnumeric():
            current_cal += float(line_clean)
        else:
            elves_list.append(current_cal)
            current_cal = 0
    elves_list.append(current_cal)
    ranking = sorted(elves_list, reverse=True)
    top_3 = sum(ranking[:3])
    print(f"Part 2: {top_3}")
    


    
    

