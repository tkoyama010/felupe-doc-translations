import numpy as np
import felupe as fem
import pyvista as pv
mesh = fem.Circle(radius=1, n=6, sections=[0, 270])
x, y = mesh.points.T
region = fem.RegionQuad(mesh)
displacement = fem.FieldPlaneStrain(region, dim=2)
boundaries = fem.dof.symmetry(displacement, axes=(True, False), x=0.0)
plotter = pv.Plotter()
actor = plotter.add_points(
    np.pad(mesh.points[boundaries["symx"].points], ((0, 0), (0, 1))),
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
