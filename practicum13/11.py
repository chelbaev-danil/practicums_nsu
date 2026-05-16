def is_valid_sudoku(board):
    '''
    Проверяет, является ли данная доска судоку допустимой.
    '''

    # строки
    for row in board:
        filled_cells = [cell for cell in row if cell != '.']
        if len(filled_cells) != len(set(filled_cells)):
            return False  

    # столбцы
    for col in range(9):
        filled_cells = [board[row][col] for row in range(9) if board[row][col] != '.']
        if len(filled_cells) != len(set(filled_cells)):
            return False  

    # подблоки 3x3
    for box_row in range(0, 9, 3):  # строки блоков (0, 3, 6)
        for box_col in range(0, 9, 3):  # столбцы блоков (0, 3, 6)
            filled_cells = []
            for i in range(3):
                for j in range(3):
                    cell = board[box_row + i][box_col + j]
                    if cell != '.':
                        filled_cells.append(cell)
            if len(filled_cells) != len(set(filled_cells)):
                return False 

    return True  

board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(is_valid_sudoku(board1))  # True
print(is_valid_sudoku(board2))  # False (две 8 в левом верхнем подблоке 3x3)