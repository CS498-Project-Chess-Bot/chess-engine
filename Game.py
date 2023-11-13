from MonteCarlos import *
import chess
if __name__ == '__main__':
    ChessPositions = ['1r2kb1r/p4p1p/1q3p2/8/2PP1Nb1/4PNP1/4KP1P/Q4B1R w k - 1 22','5r2/8/1R6/ppk3p1/2N3P1/P4b2/1K6/5B2 w - - 0 1']
    ChessPositions = ['5r2/8/1R6/ppk3p1/2N3P1/P4b2/1K6/5B2 w - - 0 1']
    print(chess.Board(ChessPositions[0]))
    print('Final State')
    print(Move(ChessPositions[0]))