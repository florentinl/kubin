# Kubin

Rubik's cube model and CFOP solver that uses a Greedy algorithm by solving each step optimally one after the other using the A* algorithm.

The package can be installed using pip

```bash
pip install git+https://github.com/florentinl/kubin
```

And then used by creating a new Rubik's Cube and manipulating it using algorithms written in the standard notation format

```python
from Kubin.Model.Cube import Cube
from Kubin.Model.AlgHandler import applyAlgorithm

cube = Cube()
print(cube)

applyAlgorithm(cube, "R U R' U R U2 R'")
print(cube)
```
