import chess
import chess.polyglot

from BoardEvaluation import evaluation

# https://github.com/astoeckl/mediumchess
# https://github.com/SebLague/Chess-AI
def moveDataOrder(board):
    moveList = []
    moveValue = []
    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            moveList.append(move)
            if board.is_check():
                x = 250
            else:
                x = 0
            if board.turn:
                moveValue.append(evaluation(board) + (150 + x))
            else:
                moveValue.append(evaluation(board) - (150 + x))
            board.pop()
        else:
            board.push(move)
            moveList.append(move)
            if board.is_check():
                x = 250
            else:
                x = 0
            if board.turn:
                moveValue.append(evaluation(board) + x)
            else:
                moveValue.append(evaluation(board) - x)
            board.pop()

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    moveOrder = []
    moves = dict(zip(moveList, moveValue))
    if board.turn:
        moves = dict(sorted(moves.items(), key=lambda item: item[1]))
    else:
        moves = dict(sorted(moves.items(), key=lambda item: item[1], reverse=True))
    for key in moves.keys():
        moveOrder.append(key)

    return moveOrder

def bookMoves(board):
    book = []
    bookmove = chess.polyglot.MemoryMappedReader("../kasparov.bin").weighted_choice(board).move
    book.append(bookmove)
    return book

def moveSearch(depth, alpha, beta, board):
    bestScore = -9999
    if depth == 0:
        return captureSearch(alpha, beta, board)
    for move in board.legal_moves:
        board.push(move)
        score = -moveSearch(depth - 1, -alpha, -beta, board)
        board.pop()
        if score >= beta:
            return score
        if score > bestScore:
            bestScore = score
        if score > alpha:
            alpha = score
    return bestScore

def captureSearch(alpha, beta, board):
    preScore = evaluation(board)
    if preScore >= beta:
        return beta
    if alpha < preScore:
        alpha = preScore

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -captureSearch(-alpha, -beta, board)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    return alpha

def moveSelect(board, depth):
    try:
        bookMoveList = bookMoves(board)
        return bookMoveList[0]
    except:
        goodMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        legalmoveList = moveDataOrder(board)
        for move in legalmoveList:
            board.push(move)
            boardValue = -moveSearch(depth - 1, -alpha, -beta, board)
            if boardValue > bestValue:
                bestValue = boardValue
                goodMove = move
            if boardValue > alpha:
                alpha = boardValue
            board.pop()
        return goodMove
    
