def print_board(board):
    for i in range(9):
        # 每隔三行加空行，方便閱讀
        if i % 3 == 0 and i != 0:
            print()
        for j in range(9):
            # 每隔三列加空格，方便閱讀
            if j % 3 == 0 and j != 0:
                print(" ", end="")
            # 打印當前數字
            print(board[i][j], end=" ")
        print()  


def is_valid_input(board, row, col, num):
    # 檢查行和列的有效性
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # 檢查 3x3 方格的有效性
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def find_empty(board):
    # 兩個迴圈遍歷盤面
    for i in range(9):
        for j in range(9):
            # 回傳第一個空白格子的座標
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    stack = []
    empty = find_empty(board)
    if empty:
        row, col = empty
        stack.append((row, col, 1))

    while stack:
        row, col, num = stack.pop()

        found_valid = False
        # 從當前數字開始到 9
        for num in range(num, 10):
            if is_valid_input(board, row, col, num):
                # 放置數字
                board[row][col] = num

                next_empty = find_empty(board)
                # 如果已經沒有空格，解決完成
                if not next_empty:
                    return True

                # 保存當前狀態
                stack.append((row, col, num + 1))

                # 移動到下一個空格
                next_row, next_col = next_empty
                stack.append((next_row, next_col, 1))
                found_valid = True
                # 找到合法的數字後跳出迴圈
                break

        # 如果沒有找到合法的數字，則回溯
        if not found_valid:
            board[row][col] = 0

    return False


sudoku_puzzle_board = [
    [0, 0, 0, 8, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 7, 0],
    [0, 0, 9, 4, 0, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 0, 3, 0, 6],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 6, 0, 0, 0, 1, 7, 0, 0],
    [9, 3, 5, 0, 1, 0, 0, 4, 0],
    [0, 0, 0, 5, 0, 8, 2, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 1, 0]
]

print("Original Board:")
print_board(sudoku_puzzle_board)

print('\nSolution:')
if solve_sudoku(sudoku_puzzle_board):
    print_board(sudoku_puzzle_board)
else:
    print("No solution")
