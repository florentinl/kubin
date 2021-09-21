from ..Model.AlgHandler import applyAlgorithm, cutAlgorithmInMoves, reverseMove, reverseAlgorithm, mirror
from heapq import *
from ..Model.Faces import Faces
class F2LSolver:
    @classmethod
    def evaluatePairDistance(cls, cube, corner, edge):
        ex, ey, ez = cube.pieces["edge"][edge].getPosition()
        eo1, eo2 = cube.pieces["edge"][edge].facesDirections
        tex, tey, tez = cube.pieces["edge"][edge].solvedPosition
        teo = cube.pieces["edge"][edge].solvedFacesDirections[0]

        cx, cy, cz = cube.pieces["corner"][corner].getPosition()
        co1, co2, co3 = cube.pieces["corner"][corner].facesDirections
        tcx, tcy, tcz = cube.pieces["corner"][corner].solvedPosition
        
        if tcy==cy and tcx==cx and tcz == cz and tex==ex and tey==ey and tez==ez and eo1==teo and co1 == Faces.D:
            return 0
        if cy == ey == 2:
            if co2 == eo1 and co3 == eo2:
                return 4
            if co2 == eo2 and co3 == mirror(eo1):
                return 4
            return 7
        return 9

    @classmethod
    def assessDistance(cls, cube):
        return sum(cls.evaluatePairDistance(cube, c,e) for c,e in [("DRF","RF"),("DLF", "LF"),("DLB", "LB"),("DRB", "RB")])

    @classmethod
    def getF2LSolution(cls, cube):
        d = cls.assessDistance(cube)
        PQ = [(d,0,d,"")]
        while PQ[0][2]!= 0:
            _, parcouru, d, prefix  = heappop(PQ)
            applyAlgorithm(cube, prefix)
            for aufMove in ["","U","U'", "U2"]:
                for preMove in ["R", "R'", "F", "F'", "L", "L'", "B", "B'"]:
                    for uMove in ["U","U'", "U2"]:
                        sequence = aufMove+preMove+uMove+reverseMove(preMove)
                        applyAlgorithm(cube, sequence)
                        d = cls.assessDistance(cube)
                        applyAlgorithm(cube, reverseAlgorithm(sequence))
                        if not aufMove and prefix and preMove == (prefix[-1] if prefix[-1] != "'" else prefix[-2:]): 
                            heappush(PQ,(parcouru+2+d,parcouru + 2, d, (prefix[:-1] if prefix[-1] != "'" else prefix[:-2]) + preMove[0]+"2"+uMove + reverseMove(preMove)))
                        else:
                            mc = 4 if aufMove else 3
                            heappush(PQ, (parcouru+mc+d,parcouru + mc, d, prefix + sequence))
                        
            applyAlgorithm(cube, reverseAlgorithm(prefix))
        return heappop(PQ)[3]