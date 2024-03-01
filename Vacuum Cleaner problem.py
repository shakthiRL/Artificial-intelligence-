print("PADMASRI-192124165")
print("Vacuum Cleaner problem")
def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def clean_grid(grid, start_row, start_col):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    to_visit = [(start_row, start_col)]

    while to_visit:
        row, col = to_visit.pop()
        
        if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
            visited.add((row, col))
            grid[row][col] = 'C'  
            
            to_visit.append((row + 1, col))
            to_visit.append((row - 1, col))
            to_visit.append((row, col + 1))
            to_visit.append((row, col - 1))

grid = [
    [0, 0, 1],
    [1, 0, 1],
    [0, 0, 0]
]
start_row = 2
start_col = 1

print("Original Grid:")
print_grid(grid)

clean_grid(grid, start_row, start_col)

print("\nCleaned Grid:")
print_grid(grid)