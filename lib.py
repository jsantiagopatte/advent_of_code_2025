import os
import numpy as np
import copy

def import_data(folder_name, file_name):
    current_dir = os.getcwd()
    file = open(os.path.join(current_dir, folder_name, file_name), 'r')
    data = file.readlines()
    data = [line.strip() for line in data]

    return data

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
    
class map_grid:
    def __init__(self, grid_string):
        self.grid = []
        for line in grid_string:
            self.grid.append(list(line))

        # Compute bounds of the grid
        self.max_row = len(self.grid)
        self.max_col = len(self.grid[0])
    
    def get_entry(self, i, j):
        return self.grid[i][j]

    def check_valid_coord(self, i, j):
        coord_check = True
        if i < 0 or i > self.max_row - 1:
            coord_check = False
        if j < 0 or j > self.max_col - 1:
            coord_check = False

        return coord_check

    def get_neighbors_coord(self, i, j):
        all_rel_neighbors = [[-1, -1], [-1, 0], [-1, +1],
                            [0, -1], [0, +1],
                            [+1, -1], [+1, 0], [+1, +1]]
        all_neighbors = []
        for rel_neighbor in all_rel_neighbors:
            all_neighbors.append([i + rel_neighbor[0], j + rel_neighbor[1]])
        
        legal_neighbors = []
        for neighbor in all_neighbors:
            if self.check_valid_coord(neighbor[0], neighbor[1]):
                legal_neighbors.append(neighbor)
        
        return legal_neighbors
    
    def print_grid(self):
        for row in self.grid:
            print(row)  