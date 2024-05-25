import felupe as fem
element = fem.QuadraticTetra()
quadrature = fem.TetrahedronQuadrature(order=5)
quadrature.plot(
    plotter=element.plot(add_point_labels=False, show_points=False),
    weighted=True,
).show()
