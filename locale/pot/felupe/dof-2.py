import pyvista as pv
right = fem.Boundary(displacement, fx=x.max())
right = fem.Boundary(displacement, fx=lambda x: np.isclose(x, x.max()))
plotter = pv.Plotter()
actor = plotter.add_points(
    mesh.points[right.points],
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
