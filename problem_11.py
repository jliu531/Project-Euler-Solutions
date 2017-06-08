# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 22:52:53 2017

@author: Jason L
"""

##parse numbers from webpage
import urllib
import re

page = urllib.request.urlopen("https://projecteuler.net/problem=11")
content = page.read().decode()

begin = content.find("\n08")
end = content.find("48<br")

numbers = content[begin:end + 2]
numbers = numbers.split("<br />\n")
grid = []
for line in numbers:
    line = re.sub('<[^>]+>', '', line) ##regex to eliminate text between html tags
    line = re.sub('\n', '', line) ##regex to eliminate '\n' text in lines
    grid.append(line)
    
grid_int = [] ##final number grid we work on will be stored in grid_int as a list of lists
for line in grid:
    line = line.split(" ")
    nums = []
    for item in line:
        nums.append(int(item))
    grid_int.append(nums)

###

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.x = len(grid[0])
        self.y = len(grid)
    
    def right_product(self, coord):
        """takes in a tuple of coordinates and gives the product of four
        adjacent numbers going right starting from and including 
        the given coordinate
        """
        i, j = coord
        if i + 3 > self.x - 1:
            return -1
        else:
            return self.grid[j][i]*self.grid[j][i + 1]*self.grid[j][i + 2]*self.grid[j][i + 3]
    
    def bottom_product(self, coord):
        """takes in a tuple of coordinates and gives the product of four
        adjacnent numbers going down starting from and including
        the given coordinate
        """
        i, j = coord
        if j + 3 > self.y - 1:
            return -1
        else:
            return self.grid[j][i]*self.grid[j + 1][i]*self.grid[j + 2][i]*self.grid[j + 3][i]
    
    def diag_product(self, coord):
        """takes in a tuple of coordinates and gives the product of four
        adjacnent numbers going down diagonally starting from and including
        the given coordinate
        """
        i, j = coord
        if i + 3 > self.x - 1:
            return -1
        if j + 3 > self.y - 1:
            return -1
        else:
            return self.grid[j][i]*self.grid[j + 1][i + 1]* \
                    self.grid[j + 2][i + 2]*self.grid[j + 3][i + 3]

### main program ###

number_grid = Grid(grid_int)
largest_num = -1
start_coordinate = ()
method = ""
for j in range(number_grid.y):
    for i in range(number_grid.x):
        if number_grid.bottom_product((i, j)) > largest_num:
            largest_num = number_grid.bottom_product((i, j))
            start_coordinate = (i, j)
            method = "down"
        if number_grid.right_product((i, j)) > largest_num:
            largest_num = number_grid.right_product((i, j))
            start_coordinate = (i, j)
            method = "right"
        if number_grid.diag_product((i, j)) > largest_num:
            largest_num = number_grid.diag_product((i, j))
            start_coordinate = (i, j)
            method = "diagonal"

print("The largest product is", largest_num, "starting at", start_coordinate, "going", method)
            
            
            
            
        
