import random
import time
import os

def create_empty_grid():
    return[[0 for _ in range(9)] for _ in range(9)]

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[subgrid_row + i][subgrid_col + j] == num:
                return False
    return True

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    time.sleep(0.1)  

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  
                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for num in numbers:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  
                        print_grid(grid)  

                        if solve_sudoku(grid):  
                            return True  

                        grid[row][col] = 0  
                        print_grid(grid)  

                return False  
    return True  

def generate_solved_sudoku():
    grid = create_empty_grid()  
    solve_sudoku(grid)  
    return grid  

solved_grid = generate_solved_sudoku()
print("Solved Sudoku in Real-Time:")
print_grid(solved_grid)