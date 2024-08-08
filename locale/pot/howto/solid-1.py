import felupe as fem

mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])

# a solid body
body = fem.SolidBody(umat=fem.NeoHooke(mu=1, bulk=2), field=field)

# a (nearly) incompressible solid body (to be used with quads and hexahedrons)
body = fem.SolidBodyNearlyIncompressible(umat=fem.NeoHooke(mu=1), field=field, bulk=5000)

internal_force = body.assemble.vector(field, parallel=False)
stiffness_matrix = body.assemble.matrix(field, parallel=False)