new_mask = np.logical_and(mask, y <= 0)
surface.apply_mask(new_mask)
plotter = pv.Plotter()
actor = plotter.add_points(
    mesh.points[surface.points],
    point_size=20,
    color="red",
)
mesh.plot(plotter=plotter, opacity=0.7).show()
