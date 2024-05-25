import felupe as fem
region = fem.RegionHexahedron(fem.Cube(a=(0, 0, 0), b=(2, 3, 1), n=(6, 11, 5)))
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries = fem.dof.uniaxial(field, axis=2, clamped=True)[0]
