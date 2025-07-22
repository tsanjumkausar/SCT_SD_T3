def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(grid, num, pos):
    row, col = pos

    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True


def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0

    return False


def input_sudoku():
    grid = []
    print("Enter the Sudoku grid (9 rows, 9 space-separated digits per row, use 0 for empty cells):")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row):
                    raise ValueError
                grid.append(row)
                break
            except ValueError:
                print("Invalid row. Enter exactly 9 digits (0–9), separated by space.")
    return grid


if __name__ == "__main__":
    sudoku_grid = input_sudoku()

    print("\nOriginal Sudoku:")
    print_grid(sudoku_grid)

    if solve(sudoku_grid):
        print("\nSolved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists.")
