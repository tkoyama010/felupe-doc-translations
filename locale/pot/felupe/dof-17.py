import felupe as fem
mesh = fem.Cube(n=5)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries = fem.dof.biaxial(
    field, clampes=(True, False), moves=(0, 0), sym=False, axes=(0, 1)
)[0]
solid = fem.SolidBodyNearlyIncompressible(fem.NeoHooke(mu=1), field, bulk=5000)
step = fem.Step(
    items=[solid],
    ramp={boundaries["move-right-0"]: fem.math.linsteps([0, 0.3], num=5),},
    boundaries=boundaries
)
job = fem.Job(steps=[step]).evaluate()
field.plot("Principal Values of Logarithmic Strain").show()
