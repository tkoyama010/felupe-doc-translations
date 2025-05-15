import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
field = fem.FieldContainer([displacement])
boundaries, loadcase = fem.dof.uniaxial(field, move=0.5, clamped=True)
