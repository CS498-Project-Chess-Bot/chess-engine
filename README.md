This is the chess engine for our Machine learning chess bot

The Node class initiates a Node in the tree with a board state, parent (None if it is the root node), a variable for whether the game has ended, a variable for whether it has been fully expanded (initially set to true if the board is an end state and has a result), the times that node has been visited, the score of that node, and its children nodes.

The Tree class is originally created and given a root node and difficulty(difficult is going to be given here as the number of iterations the Monte Carlos Tree Search will go through)

    The chooseMove function is the main function of the tree which initiates the Monte Carlos Tree Search. This goes for a number of iterations equal to the epochs. First you choose the best node to expand, then you simulate the expansion of that node, and then you backprop the score returned. After you have done that loop, you return the board state of the move from the root with the highest score. hg

