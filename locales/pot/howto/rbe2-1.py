import numpy as np
import felupe as fem

# mesh with one additional rbe2-control point
mesh = fem.Cube(n=11)
mesh.update(points=np.vstack((mesh.points, [2.0, 0.0, 0.0])))

# prevent the field-values at the center-point to be treated as dof0
mesh.points_without_cells = mesh.points_without_cells[:0]

region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
field = fem.FieldContainer([displacement])