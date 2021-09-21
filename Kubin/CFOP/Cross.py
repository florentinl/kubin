from ..Model.AlgHandler import applyAlgorithm, applyMove, reverseMove, reverseAlgorithm
from heapq import *
from ..Model.Faces import Faces
class CrossSolver:
    @classmethod
    def evaluateCubyPosition(cls, cube, cuby):
        x, y, z = cube.pieces["edge"][cuby].getPosition()
        orientation = cube.pieces["edge"][cuby].facesDirections[0]
        ex, _, ez = cube.pieces["edge"][cuby].solvedPosition
        if orientation == Faces.D: 
            return 0 if (x, z) == (ex, ez) else 1
        if orientation == Faces.U:
            return 1 if (x, z) == (ex, ez) else 2
        if (ex == 1 and orientation in [Faces.R,Faces.L]) or (ex != 1 and orientation in [Faces.F,Faces.B]):
            return 1 if x == ex or z == ez else 2
        return 2 if y == 1 else 3

    @classmethod
    def assessDistance(cls, cube):
        return sum( cls.evaluateCubyPosition(cube, edge) for edge in ["DR", "DL", "DF", "DB"])

    @classmethod
    def getCrossSolution(cls, cube):
        d = cls.assessDistance(cube)
        PQ = [(d, 0, d, "")]
        prev = None
        while PQ[0][2]!= 0:
            _, parcouru, _, prefix  = heappop(PQ)
            applyAlgorithm(cube, prefix)
            
            if prefix:
                prev = prefix[-1] if not prefix[-1] in ["2","'"] else prefix[-2]
            for move in ["U","R","F","B","D","L"]:
                if move == prev:
                    continue
                for modifier in ["","'", "2"]:
                    applyMove(cube, move+modifier)
                    d = cls.assessDistance(cube)
                    heappush(PQ,(parcouru+1+d,parcouru + 1, d, prefix+move+modifier))
                    applyMove(cube, reverseMove(move+modifier))
            applyAlgorithm(cube, reverseAlgorithm(prefix))
        return heappop(PQ)[3]