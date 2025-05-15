solid = fem.SolidBodyNearlyIncompressible(fem.NeoHooke(mu=1), field, bulk=5000)
step = fem.Step(
    items=[solid],
    ramp={
        boundaries["move-right-0"]: fem.math.linsteps([0, 0.1], num=5),
        boundaries["move-right-1"]: fem.math.linsteps([0, 0.1], num=5),
    },
    boundaries=boundaries
)
job = fem.Job(steps=[step]).evaluate()
field.plot("Principal Values of Logarithmic Strain").show()
