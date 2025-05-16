boundaries = {
    "fixed": fem.Boundary(displacement, fx=0),
    "control": fem.Boundary(displacement, fx=2, skip=(1, 0, 0)),
    "move": fem.Boundary(displacement, fx=2, skip=(0, 1, 1)),
}
table = fem.math.linsteps([0, -1, -1.5], num=5)
step = fem.Step(
    [solid, contact],
    boundaries=boundaries,
    ramp={boundaries["move"]: table},
)
job = fem.Job([step]).evaluate()
