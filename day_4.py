import os
import numpy as np
import copy

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

def check_location_valid(location, k_max, l_max):
    k = location[0]
    l = location[1]

    if k > -1 and l > -1 and k < k_max + 1 and l < l_max + 1:
        return True
    else:
        return False

def part1(folder_name, file_name):
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    data = [line.strip() for line in data]
    ans = 0
    pos_checks = [
        [-1, -1], [-1, 0], [-1, +1],
        [0, -1], [0, +1],
        [+1, -1], [+1, 0], [+1, +1]
    ]
    for i in range(len(data)):
        row = data[i]
        i_max = len(data)-1
        for j in range(len(data[i])):
            if data[i][j] == "@":
                roll_count = 0
                j_max = len(data[i])-1
                valid_pos_list = []
                for pos_check in pos_checks:
                    k = i + pos_check[0]
                    l = j + pos_check[1]
                    if check_location_valid([k,l], i_max, j_max):
                        valid_pos_list.append([k, l])
                        if data[k][l] == "@":
                            roll_count += 1
                if roll_count < 4:
                    ans += 1
    
    print(f"Part 1: {ans}")
             
                

def part2(folder_name, file_name):
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    data = [line.strip() for line in data]
    
    # Start at the beginning
    # Keep checking if a roll is removable
    # If it is, edit the map to remove the roll, back to start.
    pos_checks = [
        [-1, -1], [-1, 0], [-1, +1],
        [0, -1], [0, +1],
        [+1, -1], [+1, 0], [+1, +1]
    ]
    keep_going = True
    changes = 0
    roll_count = 0
    while keep_going:
        changes = 0
        for i in range(len(data)):
            i_max = len(data)-1
            for j in range(len(data[i])):
                if data[i][j] == "@":
                    j_max = len(data[i])-1
                    valid_pos_list = []
                    for pos_check in pos_checks:
                        k = i + pos_check[0]
                        l = j + pos_check[1]
                        if check_location_valid([k,l], i_max, j_max):
                            valid_pos_list.append([k, l])
                            if data[k][l] == "@":
                                roll_count += 1
                    if roll_count < 4:
                        data[k] = data[k][:l] + "." + data[k][l+1:] ##### Issue probably here
                        changes += 1

        if changes == 0:
            keep_going = False
    
    a = 1
    #print(f"Part 1: {ans}")

if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_4.txt"
    part2(folder_name, file_name)
    
