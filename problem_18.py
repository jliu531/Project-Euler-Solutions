# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 22:48:42 2017

@author: Jason L
"""

pyramid = [[75],
           [95, 64],
           [17, 47, 82],
           [18, 35, 87, 10],
           [20, 4, 82, 47, 65],
           [19, 1, 23, 75, 3, 34],
           [88, 2, 77, 73, 7, 63, 67],
           [99, 65, 4, 28, 6, 16, 70, 92],
           [41, 41, 26, 56, 83, 40, 80, 70, 33],
           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
           [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
           [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

class Pyramid:
    def __init__(self, pyramid):
        self.pyramid = pyramid
        self.levels = len(pyramid)
    
    def get_right_neighbor(self, coord):
        """returns the right neighbor one level down of the desginated node"""
        i, j = coord
        if i + 1 >= self.levels:
            return -1
        if j + 1 > len(self.pyramid[i + 1]) - 1:
            return -1
        return self.pyramid[i + 1][j + 1]
    
    def get_left_neighbor(self, coord):
        """returns the left neighbor one level down of the designated node"""
        i, j = coord
        if i + 1 >= self.levels:
            return -1
        return self.pyramid[i + 1][j]
    
    def get_max_neighbor(self, coord):
        """returns the maximum sum out of the possible sums of the 
        given coordinate and it's possible lower level neighbors. Also returns
        the value of the neighbor that was selected to get the maximum sum,
        and the direction of that value relative to the given coordinate"""
        i, j = coord
        a = self.get_right_neighbor(coord)
        b = self.get_left_neighbor(coord)
        if a == max([self.pyramid[i][j] + a, self.pyramid[i][j] + b]) - self.pyramid[i][j]:
            direction = "R"
        else:
            direction = "L"
        return (max([self.pyramid[i][j] + a, self.pyramid[i][j] + b]),
                max([self.pyramid[i][j] + a, self.pyramid[i][j] + b]) - self.pyramid[i][j],
                direction)
    
    def remove_level(self):
        """removes the bottom most level of the pyramid"""
        last_level = self.pyramid.pop()
        self.levels = len(self.pyramid)
        return last_level
    
    def replace_level(self, values):
        """replaces the bottom most level of the pyramid with a list of given
        values
        """
        self.pyramid[self.levels - 1] = values

### main program ###
import copy 

pyr = Pyramid(pyramid)
orig_pyr = Pyramid(copy.deepcopy(pyramid))
directions = [] # stores directions on the path that results in the largest sum
                # starting from any node

# find maximum sum
for i in range(pyr.levels - 2, -1, -1):
    maxes = []
    paths = []
    for j in range(pyr.levels - 1):
        m, p, d = pyr.get_max_neighbor((i, j))
        maxes.append(m)
        paths.append(d)
    original_level = pyr.remove_level()
    pyr.replace_level(maxes)
    directions.insert(0, paths)

# find path to get to maximum sum
path = [orig_pyr.pyramid[0][0]]
j = 0
for i in range(len(directions)):
    if directions[i][j] == "R":
        path.append(orig_pyr.get_right_neighbor((i, j)))
        j = j + 1
    else:
        path.append(orig_pyr.get_left_neighbor((i, j)))
    
        
        
    
                  
        
        