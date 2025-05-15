plotter = pv.Plotter()
actor_1 = plotter.add_points(
    mesh.points[contact.points] + displacement.values[contact.points],
    point_size=16,
    color="red",
)
actor_2 = plotter.add_points(
    mesh.points[[contact.centerpoint]] + displacement.values[[contact.centerpoint]],
    point_size=16,
    color="green",
)
field.plot(
    "Displacement", component=None, plotter=contact.plot(plotter=plotter)
).show()
