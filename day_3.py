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

def part1(folder_name, file_name):
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    bank_max = []
    for line in data:
        line = line.strip()
        bank = [batt for batt in line]
        bank_int = [int(batt) for batt in bank]
        first_batt = max(bank_int[:-1])
        first_batt_idx = bank_int.index(first_batt)
        second_batt = max(bank_int[first_batt_idx+1:])
        bank_max.append(int(str(first_batt) + str(second_batt)))
    
    print(f"Part 1: {np.sum(bank_max)}")

def part2(folder_name, file_name):
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    bank_max = []
    for line in data:
        batteries = []
        line = line.strip()
        bank = [batt for batt in line]
        bank_int = [int(batt) for batt in bank]
        batt_num = 12
        left_lim = 0
        batteries = []
        batt_current = 0
        while batt_num > 0:
            if batt_num < 12:
                left_lim = idx_prev + 1
            right_lim = -batt_num
            if batt_num == 1: # Special case last
                batt_list = bank_int[left_lim :]
            else:
                batt_list = bank_int[left_lim : right_lim+1]
            batt_current = max(batt_list)
            batteries.append(batt_current)
            idx_prev = bank_int.index(batt_current, left_lim)
            batt_num -= 1
        bank_str_list = [str(b) for b in batteries]
        bank_str = ''
        for s in bank_str_list:
            bank_str = bank_str + s
        bank_max.append(int(bank_str))


    print(f"Part 2: {np.sum(bank_max)}")

if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_3.txt"
    part2(folder_name, file_name)
    # test = split_string_multiple('123456', 1)
    # print(test)
