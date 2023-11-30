from MonteCarlos import *
import chess
if __name__ == '__main__':
    start_time_expansion = time.time()

    ChessPositions = ['1r2kb1r/p4p1p/1q3p2/8/2PP1Nb1/4PNP1/4KP1P/Q4B1R w k - 1 22','5r2/8/1R6/ppk3p1/2N3P1/P4b2/1K6/5B2 w - - 0 1']
    ChessPositions = ['5r2/8/1R6/ppk3p1/2N3P1/P4b2/1K6/5B2 w - - 0 1']
    boardFen = '8/8/2B5/pk4N1/bp6/8/1K6/8 b - - 1 8'
    board = chess.Board(ChessPositions[0])
    board.push(Move(ChessPositions[0]))
    print(board)
    print("--- %s for loop ---" % (time.time() - start_time_expansion))