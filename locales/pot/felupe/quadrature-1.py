import felupe as fem
element = fem.Line()
quadrature = fem.GaussLegendre(order=2, dim=1)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
