from Kubin.Model.Cube import Cube
from Kubin.Model.AlgHandler import applyAlgorithm
from Kubin.CFOP.CFOP import CFOPSolver

cube = Cube()
print(cube)

applyAlgorithm(cube, "R2 B F' D2 F' U D' R2 B R' D' L2 R2 U2 D B' R2 U B' U F U' B' F2 R2")
print(cube)

solution = CFOPSolver.getCFOPSolution(cube)
print(solution)
applyAlgorithm(cube, solution)
print(cube)
