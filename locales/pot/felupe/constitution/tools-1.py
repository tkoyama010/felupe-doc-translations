import felupe as fem
umat = fem.OgdenRoxburgh(fem.NeoHooke(mu=1, bulk=2), r=3, m=1, beta=0)
view = fem.ViewMaterial(
    umat,
    ux=fem.math.linsteps([1, 1.5, 1, 2, 1, 2.5, 1], num=15),
    ps=None,
    bx=None,
)
ax = view.plot(show_title=True, show_kwargs=True)
