step = fem.Step(
    items=[solid],
    ramp={boundaries["move"]: fem.math.linsteps([0, -0.35], num=10)},
    boundaries=boundaries
)
job = fem.CharacteristicCurve(steps=[step], boundary=boundaries["move"])
job.evaluate(filename="result.xdmf")

field.plot("Principal Values of Logarithmic Strain", nonlinear_subdivision=4).show()