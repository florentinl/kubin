from ..Model.Faces import Faces
from ..Model.AlgHandler import Yrot
class OLLSolver:
    
    @classmethod
    def ori(cls, cube, cuby):
        return cube.cube[cuby[0]][cuby[1]][cuby[2]].facesDirections[0]
    
    @classmethod
    def rotf(cls, f):
        return [Faces.F, Faces.U, Faces.L, Faces.B, Faces.D, Faces.R][f]

    @classmethod
    def rotate(cls, ori):
        ori[0],ori[1],ori[2],ori[3],ori[4],ori[5],ori[7],ori[6] = cls.rotf(ori[2]),cls.rotf(ori[0]),cls.rotf(ori[3]),cls.rotf(ori[1]),cls.rotf(ori[7]),cls.rotf(ori[6]),cls.rotf(ori[5]),cls.rotf(ori[4])
    
    @classmethod
    def findCase(cls, ori):
        try:
            i = [[Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.L,Faces.F,Faces.B,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.B,Faces.U,Faces.R,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.F,Faces.L,Faces.R,Faces.U,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.B,Faces.U,Faces.R,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.U,Faces.L,Faces.R,Faces.B,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.U,Faces.B,Faces.F,Faces.R,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.F,Faces.L,Faces.U,Faces.B,Faces.U,Faces.L,Faces.F,Faces.U],
            [Faces.F,Faces.L,Faces.U,Faces.B,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.L,Faces.B,Faces.U,Faces.R,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.L,Faces.U,Faces.F,Faces.R,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.F,Faces.L,Faces.R,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.U,Faces.B,Faces.F,Faces.R,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.F,Faces.L,Faces.U,Faces.B,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.L,Faces.B,Faces.U,Faces.R,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.U,Faces.L,Faces.R,Faces.B,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.L,Faces.U,Faces.U,Faces.B,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.L,Faces.U,Faces.U,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.U,Faces.R,Faces.U,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.U,Faces.U,Faces.U,Faces.U,Faces.R,Faces.L,Faces.F,Faces.B],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.L,Faces.L,Faces.F,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.U,Faces.B,Faces.U,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.F,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.L,Faces.U,Faces.U,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.F,Faces.L,Faces.U,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.U,Faces.B,Faces.F,Faces.R,Faces.U,Faces.U,Faces.U,Faces.U],
            [Faces.U,Faces.U,Faces.U,Faces.U,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.L,Faces.U,Faces.R,Faces.U,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.L,Faces.U,Faces.R,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.U,Faces.U,Faces.F,Faces.B,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.F,Faces.B,Faces.U,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.F,Faces.B,Faces.U,Faces.U,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.U,Faces.L,Faces.U,Faces.R,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.F,Faces.U,Faces.U,Faces.R,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.F,Faces.U,Faces.U,Faces.R,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.U,Faces.B,Faces.R,Faces.U,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.U,Faces.L,Faces.F,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.U,Faces.B,Faces.R,Faces.U,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.L,Faces.U,Faces.U,Faces.B,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.F,Faces.U,Faces.F,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.F,Faces.U,Faces.F,Faces.U,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.U,Faces.U,Faces.R,Faces.R,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.L,Faces.L,Faces.U,Faces.U,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.L,Faces.L,Faces.U,Faces.U,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.U,Faces.U,Faces.R,Faces.R,Faces.R,Faces.L,Faces.U,Faces.U],
            [Faces.F,Faces.B,Faces.R,Faces.R,Faces.U,Faces.L,Faces.F,Faces.U],
            [Faces.L,Faces.L,Faces.F,Faces.B,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.F,Faces.B,Faces.R,Faces.R,Faces.R,Faces.U,Faces.U,Faces.B],
            [Faces.L,Faces.L,Faces.F,Faces.B,Faces.U,Faces.L,Faces.U,Faces.B],
            [Faces.F,Faces.B,Faces.R,Faces.R,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.F,Faces.B,Faces.R,Faces.R,Faces.R,Faces.L,Faces.U,Faces.U],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.R,Faces.U,Faces.F,Faces.U],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.U,Faces.L,Faces.F,Faces.U],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.R,Faces.L,Faces.U,Faces.U],
            [Faces.L,Faces.L,Faces.R,Faces.R,Faces.U,Faces.U,Faces.F,Faces.B],
            [Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.U,Faces.F,Faces.B]].index(ori)
        except:
            i = -1
        return i

    @classmethod
    def alg(cls, case):
        return ["",
         "R U2 R2' F R F' U2' R' F R F'",
         "BL'B'LUL2F'L'FU'L'",
         "BULU'L'B'UBLUL'U'B'",
         "BULU'L'B'U'BLUL'U'B'",
         "F R U R' U' F' U' F R U R' U' F'",
         "R U R2 F R F2 U F",
         "L' U2 L U2 L F' L' F",
         "R U2 R' U2 R' F R F'",
         "R U R' U' R' F R2 U R' U' F'",
         "F U F' R' F R U' R' F' R",
         "F' L' U' L U F U F R U R' U' F'",
         "F R U R' U' F' U F R U R' U' F'",
         "F U R U2 R' U' R U R' F'",
         "R' F R U R' F' R F U' F'",
         "L'B'LR'U'RUL'BL",
         "R' F R U R' U' F' R U' R' U2 R",
         "RUR'UR'FRF'U2R'FRF'",
         "R U2 R' F' L' U2 L F R U2 R'",
         "R' U2 F R U R' U' F2 U2 F R",
         "F U R U' R' F' U2 R' U' R' F R F' U R",
         "R U R' U R U' R' U R U2 R'",
         "R U2 R2' U' R2 U' R2' U2 R",
         "R2' D' R U2 R' D R U2 R",
         "L F R' F' L' F R F'",
         "R' F' L' F R F' L F",
         "L' U' L U' L' U2 L",
         "R U R' U R U2 R'",
         "F R U R' U' F2 L' U' L U F",
         "B' R B' R2 U R U R' U' R B2",
         "R2 U R' B' R U' R2 U R B R'",
         "L'U'BULU'L'B'L",
         "R U B' U' R' U R B R'",
         "R U R' U' R' F R F'",
         "R U R' U' B' R' F R F' B",
         "R U2 R2 F R F' R U2 R'",
         "R U R' U' F' U2 F U R U R'",
         "RBU'B'U'BUB'R'",
         "L U L' U L U' L' U' L' B L B'",
         "L F' L' U' L U F U' L'",
         "R' F R U R' U' F' U R",
         "L U L' U L U2 L' F' L' U' L U F",
         "R' U' R U' R' U2 R F R U R' U' F'",
         "B' U' R' U R B",
         "BULU'L'B'",
         "F R U R' U' F'",
         "R' U' R' F R F' U R",
         "F' L' U' L U L' U' L U F",
         "F R U R' U' R U R' U' F'",
         "R B' R2 F R2 B R2 F' R",
         "R B' R B R2 U2 F R' F' R",
         "F U R U' R' U R U' R' F'",
         "R' U' R U' R' U F' U F R",
         "F R U R' U' R U' R' U R U R' F'",
         "R U' L' U R' U L U2 L F' L' F",
         "R U2 R2 U' R U' R' U2 F R F'",
         "F R U R' U' R F' L F R' F' L'",
         "L' R U R' U' L R' F R F'"
         ][case]

    @classmethod  
    def getOLLSolution(cls, cube):
        orientations  = list(map(lambda x: OLLSolver.ori(cube,x), [(0,2,2),(0,2,0),(2,2,2),(2,2,0),(2,2,1),(0,2,1),(1,2,2),(1,2,0)]))
        for i in range(4):
            n = cls.findCase(orientations)
            if n>=0:
                return ["", "U", "U2", "U'"][i] + cls.alg(n)
            cls.rotate(orientations)
    
    @classmethod
    def assertOLLSolved(cls, cube):
        return all(f == Faces.U for f in list(map(lambda x: OLLSolver.ori(cube,x), [(0,2,2),(0,2,0),(2,2,2),(2,2,0),(2,2,1),(0,2,1),(1,2,2),(1,2,0)])))