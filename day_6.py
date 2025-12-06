import os
import numpy as np
import copy
import lib

def find_next_highest_value(num, list):
    try:
        next_high = [min([x for x in list if x >= num])]
        return next_high[0]
    except:
        return 0   
    
def part1(folder_name, file_name):
    ans = 0
    data = lib.import_data(folder_name, file_name)
    # Pre-process numerical data
    number_sheet = []
    for line in data[:-1]:
        row_proc = []
        line = line.split(' ')
        for entry in line:
            if entry.isnumeric():
                row_proc.append(int(entry))
        number_sheet.append(row_proc)
    operations_raw = data[-1].split(' ')
    operation_types = ['+', '*']
    operation_sheet = []
    for operation in operations_raw:
        if operation in operation_types:
            operation_sheet.append(operation)

    np_sheet = np.transpose(np.array(number_sheet))
    answer_sheet = []
    for col, oper in zip(np_sheet, operation_sheet):
        if oper == '+':
            answer_sheet.append(np.sum(col))
        elif oper == '*':
            answer_sheet.append(np.prod(col))
    
    ans = sum(answer_sheet)
    print(f"Part 1: {ans}")



    

def part2(folder_name, file_name):
    ans = 0
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    data_clean = []
    full_sheet_np = np.array([])
    for line in data[:-1]:
        line = line.replace("\n", "")
        data_clean.append([char for char in line])

    full_sheet_np = np.array(data_clean)
    
    between_columns = False
    processed_numbers_np = copy.deepcopy(full_sheet_np)
    for i, line in enumerate(full_sheet_np):
        new_char = ''
        for j, char in enumerate(line):
            
            if char == ' ':
                full_col = full_sheet_np[:, j]
                between_columns = True
                for elem in full_col:
                    if elem != ' ':
                        between_columns = False
            else:
                between_columns = False

            if between_columns == False and char == ' ':
                processed_numbers_np[i,j] = 'x'

    grouped_numbers_list = []
    for row in processed_numbers_np:
        num_current = ''
        row_current = []
        for j, char in enumerate(row):
            if char != ' ' and j != len(line) - 1:
                num_current += char
            elif char == ' ' and j != len(line) - 1:
                row_current.append(num_current)
                num_current = ''
            elif j == len(line) - 1:
                num_current += char
                row_current.append(num_current)
                num_current = ''
        grouped_numbers_list.append(row_current)
                
    grouped_numbers_list_np = np.transpose(np.array(grouped_numbers_list))

    operations_raw = data[-1].split(' ')
    operation_types = ['+', '*']
    operation_sheet = []
    for operation in operations_raw:
        if operation in operation_types:
            operation_sheet.append(operation)

    for col, operation in zip(grouped_numbers_list_np, operation_sheet):
        col_res = 0
        col_nums =[]
        for j in range(len(col[0])):
            num_curr = ''
            for i in range(len(col)):
                char = col[i][j]
                if char != 'x':
                    num_curr += col[i][j]
            col_nums.append(int(num_curr))
        col_nums = np.array(col_nums)
        if operation == '+':
            ans += np.sum(col_nums)
        elif operation == '*':
            ans += np.prod(col_nums)
    
    print(f"Part 2: {ans}")





if __name__ == "__main__":
    folder_name = "input_files"
    file_name = "day_6.txt"
    part2(folder_name, file_name)

    
