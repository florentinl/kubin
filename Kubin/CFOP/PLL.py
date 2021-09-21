from ..Model.Faces import Faces

class PLLSolver:

    @classmethod
    def per1(cls, cube, cuby):
        return cube.pieces[["edge","corner"][len(cuby)-2]][cuby].facesDirections[1]
    
    @classmethod
    def per2(cls, cube, cuby):
        if len(cuby) == 3:
            return cube.pieces["corner"][cuby].facesDirections[2]
        return cube.pieces["edge"][cuby].facesDirections[1]

    @classmethod
    def rotf(cls, f):
        return [Faces.F, Faces.U, Faces.L, Faces.B, Faces.D, Faces.R][f]

    @classmethod
    def rotateAUF(cls, perm):
        return list(map(cls.rotf, perm))

    @classmethod
    def findCase(cls, perm):
        try:
            i = [
                [Faces.L, Faces.L, Faces.R, Faces.R, Faces.R, Faces.L, Faces.F, Faces.B],
                [Faces.L, Faces.R, Faces.B, Faces.B, Faces.R, Faces.L, Faces.F, Faces.B],
                [Faces.L, Faces.B, Faces.L, Faces.F, Faces.R, Faces.L, Faces.F, Faces.B],
                [Faces.L, Faces.L, Faces.R, Faces.R, Faces.F, Faces.R, Faces.L, Faces.B],
                [Faces.L, Faces.L, Faces.R, Faces.R, Faces.L, Faces.F, Faces.R, Faces.B],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.L, Faces.R, Faces.F, Faces.B],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.R, Faces.L, Faces.B, Faces.F],
                [Faces.B, Faces.F, Faces.B, Faces.F, Faces.R, Faces.L, Faces.F, Faces.B],
                [Faces.L, Faces.B, Faces.R, Faces.B, Faces.R, Faces.F, Faces.L, Faces.B],
                [Faces.L, Faces.B, Faces.R, Faces.B, Faces.F, Faces.L, Faces.R, Faces.B],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.F, Faces.R, Faces.B, Faces.L],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.L, Faces.B, Faces.R, Faces.F],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.B, Faces.R, Faces.L, Faces.F],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.L, Faces.F, Faces.B, Faces.R],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.B, Faces.L, Faces.F, Faces.R],
                [Faces.L, Faces.L, Faces.B, Faces.F, Faces.F, Faces.L, Faces.R, Faces.B],
                [Faces.R, Faces.L, Faces.R, Faces.L, Faces.L, Faces.R, Faces.F, Faces.B],
                [Faces.L, Faces.R, Faces.L, Faces.R, Faces.L, Faces.R, Faces.F, Faces.B],
                [Faces.L, Faces.L, Faces.R, Faces.R, Faces.L, Faces.R, Faces.B, Faces.F],
                [Faces.L, Faces.L, Faces.R, Faces.R, Faces.B, Faces.F, Faces.L, Faces.R],
                [Faces.L, Faces.R, Faces.L, Faces.R, Faces.R, Faces.B, Faces.F, Faces.L],
                [Faces.L, Faces.R, Faces.L, Faces.R, Faces.B, Faces.L, Faces.F, Faces.R],
            ].index(perm)
            a = ["so","Aa","Ab","Ua","Ub","T","F","E","Ra","Rb","Ga","Gb","Gc","Gd","Ja","Jb","Na","Nb","H","Z","Y","V"][i]
        except:
            a = ""
        return a
    
    @classmethod
    def getAlgorithm(cls, case):
        return {   "so": "",
            "Aa": "R' F R' B2 R F' R' B2 R2",
            "Ab": "R2 B2 R F R' B2 R F' R",
            "Ua": "R U' R U R U R U' R' U' R2",
            "Ub": "R2 U R U R' U' R' U' R' U R'",
            "T": "R U R' U' R' F R2 U' R' U' R U R' F'",
            "F": "L R2 U R U R2 U' R' U' R2 U' R U2 L' U R'",
            "E": "R U R D R' U R D' R' U' R D R' U' R D' R2",
            "Ra": "L U2 L' U2 L F' L' U' L U L F L2",
            "Rb": "R' U2 R U2 R' F R U R' U' R' F' R2' U'",
            "Ga": "R2 U R' U R' U' R U' R2 D U' R' U R D'",
            "Gb": "R' U' R U D' R2 U R' U R U' R U' R2 D",
            "Gc": "R2 U' R U' R U R' U R2 D' U R U' R' D",
            "Gd": "R U R' U' D R2 U' R U' R' U R' U R2 D'",
            "Ja": "L U' R' U L' U2 R U' R' U2 R",
            "Jb": "R U R' F' R U R' U' R' F R2 U' R' U'",
            "Na": "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'",
            "Nb": "R' U R U' R' F' U' F R U R' F R' F' R U' R",
            "H": "R2 U2 R U2 R2 U2 R2 U2 R U2 R2",
            "Z": "R' U' R U' R U R U' R' U R U R2 U' R'",
            "Y": "R' U' R U' L R U2 R' U' R U2 L' U R2 U R",
            "V": "R' U R' U' B' R' B2 U' B' U B' R B R"
        }[case]

    @classmethod
    def pllSolved(cls, cube):
        return [cls.per1(cube,cuby) for cuby in ["ULF", "ULB", "URF", "URB", "UR", "UL", "UF", "UB"]] == [Faces.L, Faces.L, Faces.R, Faces.R, Faces.R, Faces.L, Faces.F, Faces.B]

    @classmethod
    def getPLLSolution(cls, cube):
        perm1 = list(map(lambda x :cls.per1(cube,x), ["ULF", "ULB", "URF", "URB", "UR", "UL", "UF", "UB"]))
        perm2 = list(map(lambda x :cls.per2(cube,x), ["ULB", "URB", "ULF", "URF", "UF", "UB", "UL", "UR"]))
        perm3 = list(map(lambda x :cls.per1(cube,x), ["URB", "URF", "ULB", "ULF", "UL", "UR", "UB", "UF"]))
        perm4 = list(map(lambda x :cls.per2(cube,x), ["URF", "ULF", "URB", "ULB", "UB", "UF", "UR", "UL"]))
        for i in range(4): 
            case1 = cls.findCase(perm1)
            case2 = cls.findCase(perm2)
            case3 = cls.findCase(perm3)
            case4 = cls.findCase(perm4)
            if case1:
                return ["", "U", "U2", "U'"][i] + cls.getAlgorithm(case1)
            if case2:
                return ["", "U", "U2", "U'"][i] + cls.getAlgorithm(case2)
            if case3:
                return ["", "U", "U2", "U'"][i] + cls.getAlgorithm(case3)
            if case4:
                return ["", "U", "U2", "U'"][i] + cls.getAlgorithm(case4)
            perm1 = cls.rotateAUF(perm1)
            perm2 = cls.rotateAUF(perm2)
            perm3 = cls.rotateAUF(perm3)
            perm4 = cls.rotateAUF(perm4)
            

        