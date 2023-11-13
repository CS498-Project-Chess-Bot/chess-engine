import chess
import math
import random
from copy import deepcopy
import os


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
    def __init__(self, board, difficulty):
        self.root = Node(board)
        self.difficulty = difficulty
    def chooseMove(self):
        #limit search by iterations
        for iteration in range(self.difficulty):
            #choose a node
            node = self.selectExpansion(self.root)

            #score the node by 
            score = self.simulation(deepcopy(node.board))

            #update scores and visits for nodes along path
            self.backProp(node, score)
        
        bestMove = self.chooseBestMove(self.root, 0).board
        self.root = self.root.children[bestMove.fen()]
        return bestMove 

    def selectExpansion(self, node):
        while node.board.outcome() == None:
            if node.fullyExpanded:
                node = self.selectExpansion(self.chooseBestMove(node, 2)) #make this select expansion and see what happens
            else:
                return self.expand(node)
        else: return node

    def expand(self, node):
        legalMoves = list(node.board.legal_moves)
        for move in legalMoves:
            tempBoard = deepcopy(node.board)
            tempBoard.push(move)
            if tempBoard.fen() not in node.children.keys():
                new_node = Node(tempBoard, node)
                node.children[tempBoard.fen()] = new_node

                if len(legalMoves) == len(node.children):
                    node.fullyExpanded = True

                return new_node
        print('Error: no node found in expand function')

    def simulation(self, board):
        tempBoard = deepcopy(board)
        while tempBoard.outcome() == None:
            legalMoves = list(tempBoard.legal_moves)
            tempBoard.push(random.choice(legalMoves))
        
        if tempBoard.is_checkmate():
            if tempBoard.turn:
                return 1
            else:
                return -1
        else: return 0

        

    def backProp(self, node, score):
        while node is not None:
            node.visits += 1
            node.score += score
            node = node.parent
    
    def chooseBestMove(self, node, explorationConstant):
        highScore = -99999
        bestMoves = []


        for child in node.children.values():
            if child.board.turn == True: current_player = 1
            elif child.board.turn == False: current_player = -1
            move_score = current_player*child.score/child.visits + explorationConstant * math.sqrt(math.log(node.visits/child.visits))

            if move_score > highScore:
                highScore = move_score
                bestMoves = [child]
            elif move_score == highScore:
                bestMoves.append(child)
            
        return random.choice(bestMoves)
            

def Move(FEN, diff=1):
    board = chess.Board(FEN)
    if diff == 1: difficulty = 10000
    elif diff == 2: difficulty = 800
    else: difficulty = 600

    tree = Tree(board, difficulty)

    return tree.chooseMove()


if __name__ == '__main__':
    #create board
    board = chess.Board()
    board1 = deepcopy(board)

    diff = input("What difficulty would you like? (1 = Easy, 2 = Medium, 3 = Hard)")
    if diff == 1: difficulty = 10000
    elif diff == 2: difficulty = 800
    else: difficulty = 600

    tree = Tree(board1, difficulty)
    
    while True:
        if board1.outcome() != None:
            if board.is_checkmate():
                if board1.turn: print('Black Won')
                else: print('White Won')
            else: print('Draw')
            break
        board1 = tree.chooseMove()
        
        os.system('cls')
        print(board1)
    
    
    