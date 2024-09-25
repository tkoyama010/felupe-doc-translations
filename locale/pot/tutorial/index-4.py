move = fem.math.linsteps([0, 1], num=5)
step = fem.Step(items=[solid], ramp={boundaries["move"]: move}, boundaries=boundaries)