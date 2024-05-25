import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries = dict()
boundaries["fixed"] = fem.Boundary(field[0], fx=0, skip=(False, False, False))
boundaries["clamped"] = fem.Boundary(field[0], fx=1, skip=(True, False, False))
boundaries["move"] = fem.Boundary(field[0], fx=1, skip=(False, True, True))
umat = fem.NeoHooke(mu=1, bulk=2)
solid = fem.SolidBody(umat, field)
move = fem.math.linsteps([0, 1], num=5)
step = fem.Step(items=[solid], ramp={boundaries["move"]: move}, boundaries=boundaries)
job = fem.CharacteristicCurve(steps=[step], boundary=boundaries["move"]).evaluate()
fig, ax = job.plot(
   xlabel=r"Displacement $u_1$ in mm $\rightarrow$",
   ylabel=r"Normal Force in $F_1$ in N $\rightarrow$",
   marker="o",
)
solid.plot("Principal Values of Cauchy Stress").show()
