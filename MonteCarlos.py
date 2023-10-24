import chess
import math
import random
from copy import deepcopy

class Node():
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

        #check for end of game !!!COULD BE BUG
        if board.outcome() != None: self.end = True
        else: self.end = False

        if self.end == True: self.fullyExpanded = True
        else: self.fullyExpanded = False

        self.visits = 0 #amount of visits to node when created is 0
        self.score = 0 #amount of score is 0 when node is created
        self.children = {} #start with no children

class Tree():
    def chooseMove(self, initial_state):
        self.root = Node(initial_state)

        #limit search by iterations
        for iteration in range(1000):
            #choose a node
            node = self.selectExpansion(self.root)

            #score the node by 
            score = self.simulation(node.board)

            #update scores and visits for nodes along path
            self.backProp(node, score)
        return self.chooseBestMove(self.root, 0)

    def selectExpansion(self, node):
        pass

    def simulation(self, board):
        pass

    def backProp(self, node, score):
        pass

    def chooseBestMove(self, node, explorationConstant):
        pass



def MCTS():
    pass



if __name__ == '__main__':
    #create board
    board = chess.Board()
    board1 = deepcopy(board)
    board1.push_san("d4")
    board1.push_san("d5")

    #get legal moves 
    legalMoves = list(board.legal_moves)
    
    #make a legal move
    board1.push(legalMoves[0])
    print(board1.outcome())
    MCTS()