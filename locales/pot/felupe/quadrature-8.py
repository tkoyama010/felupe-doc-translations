import felupe as fem
element = fem.Triangle()
quadrature = fem.TriangleQuadrature(order=1)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
