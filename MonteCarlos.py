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
        self.children = {}
        

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
        while not node.isTerminal:
            if node.fullyExpanded:
                node = self.chooseBestMove(node, 2)
            else:
                return self.expand(node)
            
        return node

    def expand(self, node):
        legalMoves = list(node.board.legal_moves)
        for move in legalMoves:
            tempBoard = deepcopy(node.board)
            tempBoard = tempBoard.push(move)
            if tempBoard not in node.children:
                new_node = Node(tempBoard, node)
                node.children[tempBoard.fen()] = new_node

                if len(legalMoves) == len(node.children):
                    node.fullyExpanded = True

                return new_node
        print('Error: no node found in expand function')

    def simulation(self, board):
        while not board.is_win():
            pass

    def backProp(self, node, score):
        pass

    def chooseBestMove(self, node, explorationConstant):
        highScore = -99999
        bestMoves = []


        for child in node.children.values():
            if child.board.turn == True: current_player = 1
            elif child.boad.turn == False: current_player = -1

            move_score = current_player*child.score/child.visits + explorationConstant * math.sqrt(math.log(node.visits/child.visits))

            if move_score > highScore:
                highScore = move_score
                bestMoves = [child]
            elif move_score == highScore:
                bestMoves.append(child)

            return random.choice(bestMoves)
            



if __name__ == '__main__':
    #create board
    board = chess.Board()
    board1 = deepcopy(board)
    board1.push_san("d4")
    board1.push_san("d5")

    root = Node(board1)
    tree = Tree()

    tree.chooseBestMove(tree.root, 0)

    '''
    #get legal moves 
    legalMoves = list(board.legal_moves)
    
    #make a legal move
    board1.push(legalMoves[0])
    print(board1.outcome())
    MCTS()
    '''