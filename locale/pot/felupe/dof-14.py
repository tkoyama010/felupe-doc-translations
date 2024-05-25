import numpy as np
import felupe as fem
mesh = fem.Rectangle(a=(0, 0), b=(1, 1), n=(21, 21))
x, y = mesh.points.T
points = np.arange(mesh.npoints)[np.logical_or.reduce([x <= 0.6, y <= 0.6])]
mesh.update(cells=mesh.cells[np.all(np.isin(mesh.cells, points), axis=1)])
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])
boundaries = fem.dof.biaxial(field, clampes=(True, True))[0]
