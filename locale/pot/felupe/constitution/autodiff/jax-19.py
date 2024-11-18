import felupe as fem
umat = mat.Hyperelastic(
    mat.models.hyperelastic.storakers,
    mu=[4.5 * (1.85 / 2), -4.5 * (-9.2 / 2)],
    alpha=[1.85, -9.2],
    beta=[0.92, 0.92],
)
ax = umat.plot(
    ux=fem.math.linsteps([1, 2], 15),
    ps=fem.math.linsteps([1, 1], 15),
    bx=fem.math.linsteps([1, 1], 9),
)
