import felupe as fem
neo_hooke = fem.NeoHooke(mu=1.0)
umat = fem.OgdenRoxburgh(material=neo_hooke, r=3.0, m=1.0, beta=0.0)
ax = umat.plot(
    ux=fem.math.linsteps([1, 1.5, 1, 2, 1, 2.5, 1], num=15),
    ps=None,
    bx=None,
    incompressible=True,
)
