import felupe as fem
mesh = fem.Rectangle(a=(0, 0), b=(4, 1), n=(41, 11))
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])
