import numpy as np
import felupe as fem
x1 = np.linspace(0, 2, 3)**2
x2 = np.sqrt(np.linspace(0, 1, 3))
mesh = fem.mesh.Grid(x1, x2)
mesh.plot().show()
