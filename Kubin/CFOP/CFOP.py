from .Cross import CrossSolver 
from .F2L import F2LSolver
from .OLL import OLLSolver
from .PLL import PLLSolver
from ..Model.AlgHandler import applyMove, cutAlgorithmInMoves, applyAlgorithm, reverseAlgorithm, reverseMove

class CFOPSolver:
    
    @classmethod
    def getCFOPSolution(cls, cube):
        cs = CrossSolver.getCrossSolution(cube)
        applyAlgorithm(cube,cs)
        fs = F2LSolver.getF2LSolution(cube)
        applyAlgorithm(cube,fs)
        os = OLLSolver.getOLLSolution(cube)
        applyAlgorithm(cube, os)
        ps = PLLSolver.getPLLSolution(cube)
        applyAlgorithm(cube, ps)
        for auf in ["", "U", "U'", "U2"]:
            applyMove(cube, auf)
            if PLLSolver.pllSolved(cube):
                solution = ' '.join(cutAlgorithmInMoves(cs+fs+os+ps+auf))
                applyAlgorithm(cube, reverseAlgorithm(solution))
                return solution
            applyMove(cube,reverseMove(auf))