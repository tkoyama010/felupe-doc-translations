import felupe as fem
mesh = fem.Rectangle(a=(0, 0), b=(1, 1), n=(3, 3))
region = fem.RegionQuad(mesh)
displacement = fem.FieldPlaneStrain(region, dim=2)
field = fem.FieldContainer([displacement])
