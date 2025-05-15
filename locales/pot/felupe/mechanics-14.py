plotter = pv.Plotter()
actor_1 = plotter.add_points(
    mesh.points[mpc.points] + displacement.values[mpc.points],
    point_size=16,
    color="red",
)
actor_2 = plotter.add_points(
    mesh.points[[mpc.centerpoint]] + displacement.values[[mpc.centerpoint]],
    point_size=16,
    color="green",
)
field.plot(
    "Displacement", component=None, plotter=mpc.plot(plotter=plotter)
).show()
