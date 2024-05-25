umat = fem.OgdenRoxburgh(fem.NeoHooke(mu=1), r=3, m=1, beta=0)
view = fem.ViewMaterialIncompressible(
    umat,
    ux=fem.math.linsteps([1, 1.5, 1, 2, 1, 2.5, 1], num=15),
    ps=None,
    bx=None,
)
ax = view.plot(show_title=True, show_kwargs=True)
