import felupe as fem

mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])