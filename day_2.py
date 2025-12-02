import os

if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_2.txt"
    current_dir = os.getcwd()

    # Import file
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    invalid_ids = []

    # Get the ranges
    ranges = data[0].split(',')
    for curr_range in ranges:
        limits = curr_range.split('-')
        start = int(limits[0])
        end = int(limits[1])
        full_range = list(range(start, end+1))
        for id in full_range:
            id_str = str(id)
            length = len(id_str)
            if length%2 == 0:
                if id_str[:int(length/2)] == id_str[int(length/2):]:
                    invalid_ids.append(id)

    ans = sum(invalid_ids)
    print(f"Part 1: {ans}")