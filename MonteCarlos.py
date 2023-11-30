import chess
import math
import random
from copy import deepcopy
import os
import time


class Node():
    def __init__(self, board, moveFromParent=None, parent=None):
        self.board = board
        self.parent = parent
        self.moveFromParent = moveFromParent

        #check for end of game !!!COULD BE BUG
        if board.outcome() != None: self.end = True
        else: self.end = False

        if self.end == True: self.fullyExpanded = True
        else: self.fullyExpanded = False

        self.visits = 0 #amount of visits to node when created is 0
        self.score = 0 #amount of score is 0 when node is created
        self.children = {}
        self.childMovesNotExplored = list(self.board.legal_moves)
        

class Tree():
    def __init__(self, board, difficulty):
        self.root = Node(board)
        self.difficulty = difficulty
    def chooseMove(self):
        #limit search by iterations
        for iteration in range(self.difficulty):
            #choose a node
            #start_time_expansion = time.time()
            node = self.selectExpansion(self.root)
            #print("--- %s for select Expansion ---" % (time.time() - start_time_expansion))
            #score the node by
            #start_time_simulation = time.time()
            score = self.simulation(node.board)
            #print("--- %s for select Simulation ---" % (time.time() - start_time_simulation))
            #update scores and visits for nodes along path
            #start_time_backprop = time.time()
            self.backProp(node, score)
            #print("--- %s for select backprop ---" % (time.time() - start_time_backprop))

        bestMove = self.chooseBestMove(self.root, 0)
        #self.root = self.root.children[bestMove.fen()]
        #print(bestMove.board, bestMove.moveFromParent)
        return bestMove.moveFromParent

    def selectExpansion(self, node):
        if node.board.outcome() == None:
            if node.fullyExpanded: 
                return self.selectExpansion(self.chooseBestMove(node, 1.5)) #make this select expansion and see what happens
            else: 
                return self.expand(node)
        else: return node

    def expand(self, node: Node):
        move = random.choice(node.childMovesNotExplored)
        tempBoard = deepcopy(node.board)
        tempBoard.push(move)
        new_node = Node(tempBoard, move, node)
        node.children[tempBoard.fen()] = new_node
        node.childMovesNotExplored.remove(move)

        if not node.childMovesNotExplored: node.fullyExpanded = True

        return new_node

    def simulation(self, board):
        
        tempBoard = deepcopy(board)
    
        #start_time_expansion = time.time()
        while tempBoard.outcome() == None:
            legalMoves = list(tempBoard.legal_moves)
            #randInt = random.randint(0,len(legalMoves)-1)
            tempBoard.push(legalMoves[-1])
       # print("--- %s for loop ---" % (time.time() - start_time_expansion))
        
        if tempBoard.is_checkmate():
            if tempBoard.turn:
                return -1
            else:
                return 1
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

            if move_score > highScore or highScore == -99999:
                highScore = move_score
                bestMoves = [child]
            elif move_score == highScore:
                bestMoves.append(child)
            
        return bestMoves[0]
            

def Move(FEN, diff=1):
    board = chess.Board(FEN)
    if diff == 1: difficulty = 10001
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
    
    
    