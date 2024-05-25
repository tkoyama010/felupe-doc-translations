import numpy as np
import felupe as fem

points = np.array([
    [ 0, 0], # point 1
    [ 1, 0], # point 2
    [ 0, 1], # point 3
    [ 1, 1], # point 4
], dtype=float)

cells = np.array([
    [ 0, 1, 3, 2], # point-connectivity of first cell
])

mesh = fem.Mesh(points, cells, cell_type="quad")

# if needed, convert a FElupe mesh to a meshio-mesh
mesh_meshio = mesh.as_meshio()

# view the mesh in an interactive window
mesh.plot().show()

# take a screenshot of an off-screen view
img = mesh.screenshot(
    filename="mesh.png",
    transparent_background=True,
)