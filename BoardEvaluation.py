import chess

from PieceData import PieceDataBase

# https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec
def evaluation(board):
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

    pawnsq = sum([pieceDataBase.P[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pieceDataBase.P[i]
                           for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([pieceDataBase.N[chess.square_mirror(i)] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-pieceDataBase.N[i]
                               for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([pieceDataBase.B[chess.square_mirror(i)] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-pieceDataBase.B[i]
                               for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([pieceDataBase.R[chess.square_mirror(i)] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-pieceDataBase.R[i]
                           for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([pieceDataBase.Q[chess.square_mirror(i)] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-pieceDataBase.Q[i]
                             for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([pieceDataBase.K[chess.square_mirror(i)] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-pieceDataBase.K[i]
                           for i in board.pieces(chess.KING, chess.BLACK)])

    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq

    if board.turn:
        return eval
    else:
        return -eval
