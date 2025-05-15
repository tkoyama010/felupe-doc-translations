import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries = fem.dof.symmetry(field[0])
umat = fem.NeoHooke(mu=1, bulk=2)
solid = fem.SolidBody(umat, field)
density = 1.0
force = fem.SolidBodyForce(field, scale=density)
gravity = fem.math.linsteps([0, 2], num=5, axis=0, axes=3)
step = fem.Step(
    items=[solid, force],
    ramp={force: gravity},
    boundaries=boundaries,
)
job = fem.Job(steps=[step]).evaluate()
solid.plot("Principal Values of Cauchy Stress").show()
