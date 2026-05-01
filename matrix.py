# Create a 4x4 matrix and print the following with rest elements as '*'.
# 1. Upper Triangle  2.Lower Triangle   3.Principal Diagonal elements   4.Other Diagonal elements

# Upper Triangle
def upper_triangle(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    for i in range(0,row):
        for j in range(0,cols):
            if i <= j:
              print(f'{matrix[i][j]}  ' ,end='')
            else:
                print("*   ", end='')
        print()

# Lower Triangle
def lower_triangle(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    for i in range(0,row):
        for j in range(0,cols):
            if i >= j:
              print(f'{matrix[i][j]}  ' ,end='')
            else:
                print("*   ", end='')
        print()

# Principal diagonal elements
def pc_diagonal(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    for i in range(0,row):
        for j in range(0,cols):
            if i == j:
              print(f'{matrix[i][j]}  ' ,end='')
            else:
                print("*   ", end='')
        print()

# Other diagonal
def other_diagonal(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    for i in range(0,row):
        for j in range(0,cols):
            if (i + j) == row-1:
              print(f'{matrix[i][j]}  ' ,end='')
            else:
                print("*   ", end='')
        print()


m = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
other_diagonal(m)