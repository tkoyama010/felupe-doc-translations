import felupe as fem
element = fem.QuadraticHexahedron()
quadrature = fem.GaussLegendreBoundary(order=2, dim=3)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
