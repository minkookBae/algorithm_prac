import sys

sudoku = [[] for _ in range(10)]
zero_position = [[]]
for i in range(1,10):
    temp = list(map(int,sys.stdin.readline().split()))
    sudoku[i] = temp
    for j in range(1,10):
        if(sudoku[i][j] == 0):
            zero_position.append([i,j])

state = False

def make_candidate(pos):
    nums = [False] + [True for _ in range(9)]

    x = (pos[0]//3) * 3
    x = (pos[1]//3) * 3

def backtracking(k):
    global state

    if( k == len(zero_position) ):
        for e in sudoku:
            print(' '.join(list(map(str, e))))
        state = True
    else:
        for num in make_candidate(zero_position[k]):