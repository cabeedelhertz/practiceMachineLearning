# Program to implement a minimax AI algorithm to play a perfect tic-tac-toe game


# minimax function
def minimax(board, depth, targetDepth, isMaximizer):
    
    score = evaluate(board)
    # if maximizer won the game, return their score
    if score == 10:
        return score
    # if minimizer won the game, return their score
    if score == -10:
        return score

    if isMovesLeft(board) == False:
        return 0

    # base case to stop recursion
    if depth == targetDepth:
        return evaluate(board)
    # if it is the maximizers move
    if isMaximizer:
        bestVal = -999
        for row in range(0, len(board)):
            for col in range(0, len(board)):
                if board[row][col] == '_':
                    # make the move
                    board[row][col] = 'x'

        



# Evaluation Function
def evaluate(b):
    # check if X or O has won horizontally
    for row in range(0, len(b)):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            # if player x, value of +10
            if b[row][0] == 'x':
                return 10
            # if player o, value of -10
            elif b[row][0] == 'o':
                return -10
    # check if X or O has won vertically
    for col in range(0, len(b)):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            # if player x, value of +10
            if b[0][col] == 'x':
                return 10
            # if player o, value of -10
            elif b[0][col] == 'o':
                return -10
    # check if X or O has won diagonally
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        # if player x, value of +10
        if b[0][0] == 'x':
            return 10
        # if player o, value of -10
        elif b[0][0] == 'o':
            return -10
    
    if b[0][2] == b[1][1] and b[1][1] == b[0][2]:
        # if player x, value of +10
        if b[0][2] == 'x':
            return 10
        # if player o, value of -10
        elif b[0][2] == 'o':
            return -10
    
    # if nobody has won, return value of 0
    return 0

# function to check if there are any moves left
def isMovesLeft(b):
    for row in range(0, len(b)):
        for col in range(0, len(b)):
            if b[row][col] == '_':
                return True
    # if no open spaces found
    return False