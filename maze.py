startRow = 0
startCol = 0
start = '#'
end = '@'
maze = []

rows, cols = map(int, input("Enter rows X columns: \t").split())

for i in range(rows):
    inputStr = input().split()
    if start in inputStr:
        startCol = inputStr.index(start)
        startRow = i
    maze.append(inputStr)

print('The index of start:', startRow, startCol)

solution = [[0]*cols for _ in range(rows)]  # list to store the solution matrix
hops = 0  # the hop for min solution

# function to solve the maze
# using backtracking


def solvemaze(r, c):
    # getting the hop count with global variable
    global hops
    # if destination is reached, maze is solved
    # destination is the cell with '@'
    if ((r <= rows-1) and (c <= cols-1) and maze[r][c] == '@'):
        solution[r][c] = 1
        return True
    # checking if we can visit in this cell or not
    # and solution[r][c] == 0 is making sure that the cell is not already visited
    # maze[r][c] ==  is making sure that the cell is not blocked
    if r >= 0 and c >= 0 and r < rows and c < cols and solution[r][c] == 0 and (maze[r][c] != 0):
        # visiting a cell
        solution[r][c] = 1
        # Add step assuming it is a valid step towards solution
        hops = hops+1

        # move down
        if solvemaze(r+1, c):
            return True
        # move right
        if solvemaze(r, c+1):
            return True
        # move up
        if solvemaze(r-1, c):
            return True
        # move left
        if solvemaze(r, c-1):
            return True
        # backtracking to previous step
        solution[r][c] = 0
        # Reduce step as it is an invalid step
        hops = hops - 1
        return False
    return 0


if (solvemaze(startRow, startCol)):
    print(hops)
else:
    print("No solution")
