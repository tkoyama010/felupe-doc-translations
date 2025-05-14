import felupe as fem
mesh = fem.Circle(radius=1, n=6).expand(n=6)
x, y, z = mesh.points.T
region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
field = fem.FieldContainer([displacement])
