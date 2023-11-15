import sys
from MonteCarlos import *

if __name__ == '__main__':
    FEN = sys.argv[1]
    if sys.argv[2]: diff = sys.argv[2]
    else: diff = 1
    print(Move(FEN, diff))
