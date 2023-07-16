import collections

def isValidSudoku(board):
    # Go through the rows and see if there is repeat
    # to determine the starting position of a box, it needs to be the current
    # position i,j - i,j % 3, not needed however, see below.
    # Time complexity O(1), memory complexity O(1)

    # Checking each row in the board to see if it is valid
    # Implementation details: uses hash set to check for duplicates
    for row in board:
        contains = set()
        for element in row:
            if element == '.':
                continue
            if element in contains:
                return False
            contains.add(element)

    # Checking each column in the board to see if it is valid
    for i in range(len(board)):
        contains = set()
        for j in range(len(board)):
            if board[j][i] == '.':
                continue
            if board[j][i] in contains:
                return False
            contains.add(board[j][i])

    # Checking each of the 9 3x3 boxes in the board to see if it is valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            contains = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if board[x][y] == '.':
                        continue
                    if board[x][y] in contains:
                        return False
                    contains.add(board[x][y])
    return True

print(isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))

# This is the neetcode solution
# Using three hashmaps which have the key as row/col/square and value of hashset that represents the values in
# each col/row/square
def is_valid_sudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            if board[row][col] in cols[col] or board[row][col] in rows[row] or board[row][col] in squares[(row//3, col//3)]:
                return False
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            squares[(row//3, col//3)].add(board[row][col])
    return True


print(is_valid_sudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))


