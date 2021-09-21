from .FlatCubeWriter import FlatCubeWriterFactory
from .Faces import Faces

class Cube:

    def __init__(self, writer = FlatCubeWriterFactory.createFlatCubeWriter()):
        self.writer = writer
        
        self.rotations = [[Faces.R, Faces.B, Faces.U, Faces.L, Faces.F, Faces.D],
                          [Faces.F, Faces.U, Faces.L, Faces.B, Faces.D, Faces.R],
                          [Faces.D, Faces.R, Faces.F, Faces.U, Faces.L, Faces.B],
                          [Faces.R, Faces.F, Faces.D, Faces.L, Faces.B, Faces.U],
                          [Faces.B, Faces.U, Faces.R, Faces.F, Faces.D, Faces.L],
                          [Faces.U, Faces.L, Faces.F, Faces.D, Faces.R, Faces.B]]
        self.pieces = {
            "edge": {
                "UR": Cuby([Faces.U, Faces.R]),
                "UL": Cuby([Faces.U, Faces.L]),
                "UF": Cuby([Faces.U, Faces.F]),
                "UB": Cuby([Faces.U, Faces.B]),
                "DR": Cuby([Faces.D, Faces.R]),
                "DL": Cuby([Faces.D, Faces.L]),
                "DF": Cuby([Faces.D, Faces.F]),
                "DB": Cuby([Faces.D, Faces.B]),
                "LF": Cuby([Faces.L, Faces.F]),
                "LB": Cuby([Faces.L, Faces.B]),
                "RF": Cuby([Faces.R, Faces.F]),
                "RB": Cuby([Faces.R, Faces.B])
            },
            "corner": {
                "ULF": Cuby([Faces.U, Faces.L, Faces.F]),
                "ULB": Cuby([Faces.U, Faces.L, Faces.B]),
                "URF": Cuby([Faces.U, Faces.R, Faces.F]),
                "URB": Cuby([Faces.U, Faces.R, Faces.B]),
                "DLF": Cuby([Faces.D, Faces.L, Faces.F]),
                "DLB": Cuby([Faces.D, Faces.L, Faces.B]),
                "DRF": Cuby([Faces.D, Faces.R, Faces.F]),
                "DRB": Cuby([Faces.D, Faces.R, Faces.B])
            },
            "center":{
                "U": Cuby([Faces.U]),
                "D": Cuby([Faces.D]),
                "R": Cuby([Faces.R]),
                "L": Cuby([Faces.L]),
                "F": Cuby([Faces.F]),
                "B": Cuby([Faces.B])
            }
        }
        
        self.cube = [
            [
                [self.pieces["corner"]["DLB"], self.pieces["edge"]["DL"] , self.pieces["corner"]["DLF"]],
                [self.pieces["edge"]["LB"]   , self.pieces["center"]["L"], self.pieces["edge"]["LF"]   ],
                [self.pieces["corner"]["ULB"], self.pieces["edge"]["UL"] , self.pieces["corner"]["ULF"]]
            ],
            [
                [self.pieces["edge"]["DB"]   , self.pieces["center"]["D"], self.pieces["edge"]["DF"]   ],
                [self.pieces["center"]["B"]  , None                      , self.pieces["center"]["F"]  ],
                [self.pieces["edge"]["UB"]   , self.pieces["center"]["U"], self.pieces["edge"]["UF"]   ]
            ],
            [
                [self.pieces["corner"]["DRB"], self.pieces["edge"]["DR"] , self.pieces["corner"]["DRF"]],
                [self.pieces["edge"]["RB"]   , self.pieces["center"]["R"], self.pieces["edge"]["RF"]   ],
                [self.pieces["corner"]["URB"], self.pieces["edge"]["UR"] , self.pieces["corner"]["URF"]]
            ]
        ]
    def rotmat(self, mat, dir):
        if dir == 1:
            mat[0][0],mat[0][1],mat[0][2],mat[1][2],mat[2][2],mat[2][1],mat[1][0],mat[2][0] = mat[0][2],mat[1][2],mat[2][2],mat[2][1],mat[2][0],mat[1][0],mat[0][1],mat[0][0]
        else:
            mat[0][2],mat[1][2],mat[2][2],mat[2][1],mat[2][0],mat[1][0],mat[0][1],mat[0][0] = mat[0][0],mat[0][1],mat[0][2],mat[1][2],mat[2][2],mat[2][1],mat[1][0],mat[2][0]

    def Rmove(self, direction):
        Rslice = self.cube[2]
        for i in range(3):
            for j in range(3):
                Rslice[i][j].rotate(self.rotations, Faces.R, direction)
        self.rotmat(Rslice, -direction)

    def Lmove(self, direction):
        Lslice = self.cube[0]
        for i in range(3):
            for j in range(3):
                Lslice[i][j].rotate(self.rotations, Faces.L, direction)
        self.rotmat(Lslice, direction)
    
    def Umove(self, direction):
        Uslice = [self.cube[i][2] for i in range(3)]
        self.rotmat(Uslice, direction)
        for i in range(3):
            for j in range(3):
                Uslice[i][j].rotate(self.rotations, Faces.U, direction)      
    
    def Dmove(self, direction):
        Dslice = [self.cube[i][0] for i in range(3)]
        self.rotmat(Dslice, -direction)
        for i in range(3):
            for j in range(3):
                Dslice[i][j].rotate(self.rotations, Faces.D, direction)         

    def Fmove(self, direction):
        Fslice = [[self.cube[i][j][2] for j in range(3)][::-1] for i in range(3)]
        self.rotmat(Fslice, direction)
        for i in range(3):
            for j in range(3):
                Fslice[i][j].rotate(self.rotations, Faces.F, direction)
                self.cube[i][j][2] = Fslice[i][::-1][j]

    def Bmove(self, direction):
        Bslice = [[self.cube[i][j][0] for j in range(3)][::-1] for i in range(3)]       
        self.rotmat(Bslice, -direction)
        for i in range(3):
            for j in range(3):
                Bslice[i][j].rotate(self.rotations, Faces.B, direction)
                self.cube[i][j][0] = Bslice[i][::-1][j]
    
    def Mmove(self, direction):
        Mslice = self.cube[1]
        self.rotmat(Mslice, direction)
        for i in range(3):
            for j in range(3):
                Mslice[i][j].rotate(self.rotations)
    def __repr__(self):
        string = ""

        U = [[None for _ in range(3)] for _ in range(3)]
        R = [[None for _ in range(3)] for _ in range(3)]
        B = [[None for _ in range(3)] for _ in range(3)]
        L = [[None for _ in range(3)] for _ in range(3)]
        F = [[None for _ in range(3)] for _ in range(3)]
        D = [[None for _ in range(3)] for _ in range(3)]

        for pieceType in ["edge", "center", "corner"]:
            for piece in self.pieces[pieceType]:
                cuby = self.pieces[pieceType][piece]
                x, y, z = cuby.getPosition()
                for let, vec in zip(piece,cuby.facesDirections):
                    if vec == Faces.U:
                        U[z][x] =  let
                    elif vec == Faces.D:
                        D[z][2-x] = let
                    elif vec == Faces.R:
                        R[z][2-y] = let
                    elif vec == Faces.L:
                        L[z][y] = let
                    elif vec == Faces.F:
                        F[2-y][x] = let
                    elif vec == Faces.B:
                        B[y][x] = let
                    else:
                        assert False, f"Vector : {vec}"
        for line in B:
            string += "    " + ''.join(line) + "\n"
        string += "\n"
        for l, u, r, d in zip(L,U,R,D):
            string += ''.join(l) + ' ' + ''.join(u) + ' ' + ''.join(r) + ' ' + ''.join(d) + "\n"
        string += "\n"
        for line in F:
            string += "    " + ''.join(line) + "\n"

        colorized_string = self.writer.writeCube(string)
        return colorized_string

class Cuby:
    def __init__(self, faces):
        self.facesDirections = faces
        self.solvedFacesDirections = faces[:]
        self.solvedPosition = self.getPosition()
    
    def getPosition(self):  
        if Faces.R in self.facesDirections:
            x = 2
        elif Faces.L in self.facesDirections:
            x = 0
        else:
            x = 1

        if Faces.U in self.facesDirections:
            y = 2
        elif Faces.D in self.facesDirections:
            y = 0
        else:
            y = 1

        if Faces.F in self.facesDirections:
            z = 2
        elif Faces.B in self.facesDirections:
            z = 0
        else:
            z = 1
        
        return x, y, z
     
    def rotate(self, rotations, move, direction):
        for i, f in enumerate(self.facesDirections):
            if direction == 1:
                self.facesDirections[i] = rotations[move][f]
            else:
                self.facesDirections[i] = rotations[move+3 if move < 3 else move - 3][f]