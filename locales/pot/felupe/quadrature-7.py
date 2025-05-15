import felupe as fem
element = fem.ArbitraryOrderLagrangeElement(order=5, dim=3)
quadrature = fem.GaussLegendreBoundary(order=5, dim=3)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
