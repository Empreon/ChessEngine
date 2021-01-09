import chess
from PieceData import pieceDataBase

def evaluation(board):
    # https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec
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

    material = pieceDataBase.pawnValue * (wp - bp) + \
               pieceDataBase.kingValue * (wn - bn) + \
               pieceDataBase.bishopValue * (wb - bb) + \
               pieceDataBase.rookValue * (wr - br) + \
               pieceDataBase.queenValue * (wq - bq)

    if board.turn:
        return material
    else:
        return -material
