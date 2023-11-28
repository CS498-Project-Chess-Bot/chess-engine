import sys
from MonteCarlos import *



if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print("Error, no FEN given")
        sys.exit()
    FEN = sys.argv[1]
    if len(sys.argv) > 2: diff = sys.argv[2]
    else: diff = 1
    print(Move(FEN, diff))
