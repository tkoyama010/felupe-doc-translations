import felupe as fem
import numpy as np
import pyvista as pv
m = fem.Rectangle(n=2)
mesh = m.copy()
mesh.points[-1, 0] += 0.5
edges = fem.RegionQuadBoundary(mesh)
start = fem.Field(edges, values=mesh.points).interpolate()
(direction,) = edges.tangents
start = np.insert(start, len(start), 0, axis=0)
direction = np.insert(direction, len(direction), 0, axis=0)
normal = np.insert(edges.normals, len(edges.normals), 0, axis=0)
plotter = pv.Plotter()
actor = plotter.add_arrows(
    start.reshape(3, -1).T,
    direction.reshape(3, -1).T,
    show_scalar_bar=False,
    mag=1 / 7,
    color="red",
    label="tangents",
)
actor = plotter.add_arrows(
    start.reshape(3, -1).T,
    normal.reshape(3, -1).T,
    show_scalar_bar=False,
    mag=1 / 7,
    color="green",
    label="normals",
)
actor = plotter.add_legend()
mesh.plot(plotter=plotter, style="wireframe").show()
