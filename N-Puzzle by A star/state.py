'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''

import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n**3):  # makes n^3 random moves to mix the tiles
        if_legal(s,m[random.randrange(4)])
    return [[4, 3, 7, 5, 8, 6, 1, 0, 2],""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0

'''
Author Shimon Mizrahi 203375563
I ran the program with s=[[4,3,7,5,8,6,1,0,2],""],
At first I used the given heuristic function, 
Because it is not really accurate it took the computer more than a few seconds to calculate.
I received a large number of steps from attaching what I received:
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 40175, 16920]
after that i ran the program with a function in which I built the more accurate heuristics.
I got fast results with a really small amount of steps:
Attaches the results
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^^<v>^<'], 623, 262]
It can be seen that this is a significant difference!!!!
It is therefore very important to choose as good a legal function as possible.
Thank you :)
'''
                                    # Purpose of this heuristic function is:
                                    #Return the total moves in the program in the Manhattan method.

def hdistance(s):                   # the heuristic value of s
    n=int(math.sqrt(len(s)))        # n = the number of row or column in matrix
    target_row=0                    # target_row will store the row of target element
    target_column=0                 # target_column will store the column of target element
    temp_row=0                      # temp_row will store the calculation of row current element
    temp_column=0                   # temp_column will store the calculation of column current element
    c=0                             # c is the number of Manhattan moves
    for i in range(0,len(s[0])):    # We will run on each slot
        if s[0].index(i)!=i:        # Enter the loop only when the place is not equal
            target_row=i//n         # target store the row
            target_column=i%n       # target store the column
            temp_row=s[0].index(i)//n # current store the row
            temp_column=s[0].index(i)%n # current store the column
            c += abs(target_row-temp_row) + abs(target_column-temp_column) # Total steps: |target_row - temp_row|
                                                                           # + |target_column - temp_column|
    return c                             # return total moves.


'''
def hdistance(s):
    c=0
    for i in range(1,len(s[0])):
        if s[0].index(i)!=i:
            c+=1
    return c
'''

