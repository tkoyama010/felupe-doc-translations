import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
u = displacement.interpolate()
dudX = displacement.grad()
