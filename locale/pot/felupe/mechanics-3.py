import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries = fem.dof.symmetry(field[0])
umat = fem.NeoHooke(mu=1, bulk=2)
solid = fem.SolidBody(umat, field)
gravity = fem.SolidBodyGravity(field, density=1.0)
table = fem.math.linsteps([0, 1], num=5, axis=0, axes=3)
step = fem.Step(
    items=[solid, gravity],
    ramp={gravity: 2 * table},
    boundaries=boundaries,
)
job = fem.Job(steps=[step]).evaluate()
solid.plot("Principal Values of Cauchy Stress").show()
