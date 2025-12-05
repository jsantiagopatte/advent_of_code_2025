import os
import numpy as np
import copy
import lib

def split_ranges_food(data):
    ranges = []
    food_ids = []
    current = "ranges"
    for item in data:
        if item == '':
            current = "food"
            continue
        if current == "ranges":
            ranges.append(item)
        else:
            food_ids.append(item)
    
    return ranges, food_ids

def question_range(id, range):
    if id > range[0] and id < range[1]:
        return True
    else:
        return False
    
def process_range_str(data):
    ranges_list = []
    for line in data:
        if line !='':
            range_str = line.split('-')
            ranges_list.append([int(range_str[0]), int(range_str[1])])
        else:
            break
    
    return ranges_list

def new_range_generator(range, range_target):
    min_c = min(range)
    max_c = max(range)
    min_t = min(range_target)
    max_t = max(range_target)
    ranges_result = []

    # If range is on the left: max_c < min_t
    if max_c < min_t:
        min_r = min_c
        max_r = max_c
        ranges_result = [[min_r, max_r]]
    # If range is partly on left: min_c < min_t and (max_c < max_t and max_c > min_t)
    elif min_c < min_t and (max_c <= max_t and max_c >= min_t):
        min_r = min_c
        max_r = min_t - 1
        ranges_result = [[min_c, max_r]]
    # If range is in the middle: min_c > min_t and max_c < max_t
    elif min_c >= min_t and max_c <= max_t:
        return None
    # If range is partly on the right: max_c > max_t and (min_c > min_t and min_c < max_t)
    elif max_c > max_t and (min_c >= min_t and min_c <= max_t):
        min_r = max_t + 1
        max_r = max_c
        ranges_result = [[min_r, max_r]]
    # If range is on the right: min_c > max_t
    elif min_c > max_t:
        min_r = min_c
        max_r = max_c
        ranges_result =[[min_r, max_r]]
    # If range is larger than target on both sides min_c < min_t and max_c > max_t
    elif min_c < min_t and max_c > max_t:
        min_r1 = min_c
        max_r1 = min_t - 1
        min_r2 = max_t + 1
        max_r2 = max_c
        ranges_result = [[min_r1, max_r1], [min_r2, max_r2]]

    return ranges_result

    
def part1(folder_name, file_name):
    ans = 0
    data = lib.import_data(folder_name, file_name)
    fresh_ranges_str, food_ids_str = split_ranges_food(data)
    food_ids = map(int, food_ids_str)
    fresh_ranges = []
    for fresh_range in fresh_ranges_str:
        fresh_range_lims = fresh_range.split('-')
        fresh_range_start = int(fresh_range_lims[0])
        fresh_range_end = int(fresh_range_lims[1])
        fresh_ranges.append([fresh_range_start, fresh_range_end])
    fresh_food_ids = []
    for food_id in food_ids:
        for fresh_range in fresh_ranges:
            if question_range(food_id, fresh_range) and food_id not in fresh_food_ids:
                fresh_food_ids.append(food_id)
                ans += 1
    
    print(f"Part 1:{ans}")

def part2(folder_name, file_name):
    data = lib.import_data(folder_name, file_name)
    ranges_list_full = process_range_str(data)
    
    ranges_old = ranges_list_full
    ranges_new = []
    diff = 1
    while diff > 0:
        ranges_new = []
        for range_current in ranges_old:
            for range_target in ranges_old:
                split = False
                ranges_test = new_range_generator(range_current, range_target)
                if ranges_test is not None:
                    for r in ranges_test:
                        if r != range_current:
                            split = True
                        if r not in ranges_new:
                            ranges_new.append(r)
            if split == True and range_current in ranges_new:
                ranges_new.remove(range_current)
        
        diff +=1
        print(diff)
        if ranges_new == ranges_old:
            diff = 0

        ranges_old = ranges_new 
    
    ranges_final = ranges_old
    # Calculate total of all ranges
    ans = 0
    for range_food in ranges_final:
        ans += (range_food[1] - range_food[0]) + 1

    print(ranges_final)
    print(f"Part 2: {ans}")





if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_5.txt"
    part2(folder_name, file_name)
    #test = new_range_generator([10,11], [5, 10])
    #print(test)\
    
