import numpy as np
import felupe as fem
points = np.array(
    [[0.0, 0.0], [0.5, 0.1], [1.0, 0.2], [0.0, 1.0], [0.5, 0.9], [1.0, 0.8]]
)
cells = np.array([[0, 1, 4, 3], [1, 2, 5, 4]])
mesh = fem.Mesh(points, cells, cell_type="quad")
mesh.plot().show()
