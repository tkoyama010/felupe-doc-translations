axes = fem.Boundary(displacement, fx=0, fy=0, mode="or")
plotter = pv.Plotter()
actor = plotter.add_points(
    mesh.points[axes.points],
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
