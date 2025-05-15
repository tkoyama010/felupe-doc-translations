import felupe as fem
umat = fem.Hyperelastic(
    fem.ogden_roxburgh,
    material=fem.neo_hooke,
    r=3,
    m=1,
    beta=0.1,
    mu=1,
    nstatevars=1
)
ux = fem.math.linsteps(
    [1, 2.5, 1, 3.5, 1], num=[15, 15, 25, 25]
)
ax = umat.plot(ux=ux, bx=None, ps=None, incompressible=True)
