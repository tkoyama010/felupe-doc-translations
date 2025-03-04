import felupe as fem
import numpy as np
import pyvista as pv
m = fem.Cube(n=2)
mesh = m.copy()
mesh.points[-1, 0] += 0.5
faces = fem.RegionHexahedronBoundary(mesh, mask=m.x == m.x.max())
start = fem.Field(faces, values=mesh.points).interpolate()
direction, direction_2 = faces.tangents
plotter = pv.Plotter()
actor = plotter.add_arrows(
    start.reshape(3, -1).T,
    direction.reshape(3, -1).T,
    show_scalar_bar=False,
    mag=1 / 7,
    color="red",
    label="tangents (1)",
)
actor = plotter.add_arrows(
    start.reshape(3, -1).T,
    direction_2.reshape(3, -1).T,
    show_scalar_bar=False,
    mag=1 / 7,
    color="green",
    label="tangents (2)",
)
actor = plotter.add_arrows(
    start.reshape(3, -1).T,
    faces.normals.reshape(3, -1).T,
    show_scalar_bar=False,
    mag=1 / 7,
    color="blue",
    label="normals",
)
plotter.add_legend()
mesh.plot(plotter=plotter, style="wireframe").show()
