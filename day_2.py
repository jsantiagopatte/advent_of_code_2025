import os
import numpy as np

def get_factors(num):
    '''
    Returns all the integers the given integer is divisible by. 
    '''
    result = []
    for i in range(1, num):
        if num % i == 0:
            result.append(i)
    
    return result

def split_string_multiple(string, split_length):
    '''
    Splits the string into multiple strings of the given lenght.
    '''
    split_strings = []
    split_points = list(range(split_length, len(string) + 1, split_length))
    prev_end = 0
    for split_end in split_points:
        new_str = string[prev_end:split_end]
        split_strings.append(new_str)
        prev_end = prev_end + split_length
    
    return split_strings



def part1():
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

def part2():
        #### Part 2
        folder_name = "input_files"
        file_name = "day_2.txt"
        current_dir = os.getcwd()
        file = open(os.path.join(current_dir, folder_name, file_name), 'r')
        data = file.readlines()
        invalid_ids = []

        ranges = data[0].split(',')
        for curr_range in ranges:
            limits = curr_range.split('-')
            start = int(limits[0])
            end = int(limits[1])
            full_range = list(range(start, end+1))
            for id in full_range:
                factors = get_factors(len(str(id)))
                for factor in factors:
                    split_len = factor
                    all_str_splits = split_string_multiple(str(id), split_len)
                    if all(item == all_str_splits[0] for item in all_str_splits):
                        invalid_ids.append(id)
                        break
        
        ans = sum(invalid_ids)
        print(f"Part 2: {ans}")



if __name__ == "__main__":
    part2()
    # test = split_string_multiple('123456', 1)
    # print(test)
