import numpy as np
import felupe as fem
mesh = fem.Cube(n=3)
mesh.update(points=np.vstack([mesh.points, [2.0, 0.5, 0.5]]))
mesh.points_without_cells = mesh.points_without_cells[:-1]
region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
field = fem.FieldContainer([displacement])
umat = fem.NeoHooke(mu=1.0, bulk=2.0)
solid = fem.SolidBody(umat=umat, field=field)
