# prepare a step with substeps
move = fem.math.linsteps([0, 3], num=10)
step = fem.Step(
    items=[matrix, fiber],
    ramp={boundaries["move"]: move},
    boundaries=boundaries,
)

# take care of the x0-argument
job = fem.Job(steps=[step])
job.evaluate(x0=field)

fields[1].plot(
    "Principal Values of Logarithmic Strain",
    show_undeformed=False,
    plotter=fields[0].plot(
        "Principal Values of Logarithmic Strain", show_undeformed=False
    ),
).show()