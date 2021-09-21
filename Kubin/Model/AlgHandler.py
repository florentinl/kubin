from ..Model.Faces import Faces


def Yrot(alg, rot):
    if rot == 0 or rot == 4:
        return alg
    moves = cutAlgorithmInMoves(alg)
    rotDict = {"R":"F","F":"L","L":"B","B":"R","D":"D","U":"U"}
    for _ in range(rot):
        moves = map(lambda m: rotDict[m[0]]+m[1:], moves)
    return ''.join(list(moves))


def mirror(f):
    if f == Faces.F:
        return Faces.B
    if f == Faces.B:
        return Faces.F
    if f == Faces.R:
        return Faces.L
    if f == Faces.L:
        return Faces.R
    if f == Faces.D :
        return Faces.U
    if f == Faces.U :
        return Faces.D

def cutAlgorithmInMoves(algorithm):
    moveList = []
    for i in algorithm:
        if i in "FRBLDUMr":
            moveList.append(i)
        elif i in "'2":
            move = moveList.pop() + i
            moveList.append(move)
    return moveList

def moveCount(algorithm):
    return len(cutAlgorithmInMoves(algorithm))

def applyMove(cube, move):
    if move == "":
        return
    turns = 1
    if len(move) == 1:
        direction = 1
    elif move[1] == "'":
        direction = -1
    else:
        turns = 2
        direction = 1
    move = move[0]
    if move == "R":
        fun = cube.Rmove
    elif move == "U":
        fun = cube.Umove
    elif move == "F":
        fun = cube.Fmove
    elif move == "D":
        fun = cube.Dmove
    elif move == "L":
        fun = cube.Lmove
    elif move == "B":
        fun = cube.Bmove
    elif move == "M":
        fun = cube.Mmove
    elif move == "r":
        fun = cube.Rwmove

    for _ in range(turns):
        fun(direction)
def applyAlgorithm(cube, algorithm):
    moves = cutAlgorithmInMoves(algorithm)
    applyMoveList(cube, moves)

def applyMoveList(cube, moves):
    for move in moves:
        applyMove(cube, move)

def reverseMove(move):
    if move == "":
        return ""
    if len(move) == 1:
        return move+"'"
    if move[1] == "2":
        return move
    return move[0]

def reverseAlgorithm(algorithm):
    return ''.join(reverseMoveList(algorithm))

def reverseMoveList(algorithm):
    reversedAlgorithm = []
    for move in cutAlgorithmInMoves(algorithm):
        reversedAlgorithm.append(reverseMove(move))
    reversedAlgorithm = reversedAlgorithm[::-1]
    return reversedAlgorithm