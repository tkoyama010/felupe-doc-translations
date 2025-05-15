import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries, loadcase = fem.dof.uniaxial(field, clamped=True)
umat = fem.NeoHooke(mu=1, bulk=2)
solid = fem.SolidBody(umat, field)
table = fem.math.linsteps([0, 1], num=5)
step = fem.Step(
    items=[solid],
    ramp={boundaries["move"]: table},
    boundaries=boundaries,
)
job = fem.Job(steps=[step]).evaluate()
solid.plot("Principal Values of Cauchy Stress").show()
