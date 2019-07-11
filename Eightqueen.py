num = 0

def check(board, row, col):
    i = 0
    while i < row:
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
        i += 1
    return True

def eightqueen(board, row):
    board_size = len(board)
    if row == board_size:
        global num
        num += 1
        print(board)
        return 
    col = 0
    while col < board_size:
        if check(board, row, col):
            board[row] = col
            eightqueen(board, row + 1)
        col += 1
    return 

def main(size):
    myboard = []
    for i in range(size):
        myboard.append(0)
    eightqueen(myboard, 0)
    print('There are %d combinations of %d queens on a %d cells chessboard' %(num, size, size ** 2))
    
if __name__ == "__main__":
    size = int(input('Input the size of board: '))
    main(size)