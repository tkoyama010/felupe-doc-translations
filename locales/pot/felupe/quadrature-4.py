import felupe as fem
element = fem.ArbitraryOrderLagrangeElement(order=5, dim=2)
quadrature = fem.GaussLegendre(order=5, dim=2)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
