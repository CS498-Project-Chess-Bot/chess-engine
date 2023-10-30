import chess
from copy import deepcopy

if __name__ == '__main__':
    board = chess.Board()
    board1 = deepcopy(board)
    board1.push_san("d4")
    #board1.push_san("d5")
    #moves = dict(zip(board.legal_moves, None))
    print(list(board.legal_moves))

    '''
    for move in list(self.board.legal_moves):
            self.children
        childs = [board.push(move) for move in list(self.board.legal_moves)]
        print(childs)
        self.children = dict(zip(childs, None)) #start with no children
    '''