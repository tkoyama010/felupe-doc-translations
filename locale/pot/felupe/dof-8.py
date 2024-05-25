left = fem.Boundary(displacement, fx=x.min(), value=-0.2)
left.update(-0.3)
plotter = pv.Plotter()
actor = plotter.add_points(
    mesh.points[left.points],
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
