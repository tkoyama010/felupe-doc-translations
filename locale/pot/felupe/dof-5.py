mask = np.logical_and(np.isclose(x**2 + y**2, 1), x >= 0)
surface = fem.Boundary(displacement, mask=mask)
plotter = pv.Plotter()
actor = plotter.add_points(
    mesh.points[surface.points],
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
