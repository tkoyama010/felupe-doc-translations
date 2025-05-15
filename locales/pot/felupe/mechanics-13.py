boundaries = {"fixed": fem.Boundary(displacement, fx=0)}
load = fem.PointLoad(field, points=[-1])
table = fem.math.linsteps([0, 1], num=5, axis=0, axes=3)
step = fem.Step(
    [solid, mpc, load], boundaries=boundaries, ramp={load: table}
)
job = fem.Job([step]).evaluate()
