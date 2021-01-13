import chess
import chess.polyglot

from BoardEvaluation_1 import evaluation

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def bookMove(board):
    book = []
    move = chess.polyglot.MemoryMappedReader("kasparov.bin").weighted_choice(board).move
    book.append(move)
    return book

def moveDeneme(board, move, list):
    board.push(move)
    if board.is_game_over():
        list.append(evaluation(board))

def minimaxDeneme(board):
    minValues = []
    moves = board.legal_moves
    allValues = []
    for move0 in board.legal_moves:
        moveDeneme(board, move0, allValues)
        if not board.is_game_over():
            for move1 in board.legal_moves:
                moveDeneme(board, move1, allValues)
                if not board.is_game_over():
                    for move2 in board.legal_moves:
                        board.push(move2)
                        allValues.append(evaluation(board))
                        board.pop()
                board.pop()
        board.pop()
        minValues.append(min(allValues))
        allValues.clear()

    baDict = dict(zip(moves, minValues))
    return baDict

def moveSelect(board):
    try:
        bookMoveList = bookMove(board)
        return bookMoveList[0]
    except:
        print("move from algorithm")
        maxMove = keywithmaxval(minimaxDeneme(board))
        return maxMove

chessboard = chess.Board("r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4")
