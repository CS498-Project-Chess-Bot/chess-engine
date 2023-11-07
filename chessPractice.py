import chess
from copy import deepcopy

if __name__ == '__main__':
    board = chess.Board('3k1b2/4p1p1/4B1r1/p1p3Pn/P7/2q5/1P6/R2Kr1B1 w - - 8 51')
    board1 = deepcopy(board)
    #moves = dict(zip(board.legal_moves, None))
    print(board1.is_checkmate())

    '''
    for move in list(self.board.legal_moves):
            self.children
        childs = [board.push(move) for move in list(self.board.legal_moves)]
        print(childs)
        self.children = dict(zip(childs, None)) #start with no children
    '''