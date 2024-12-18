import pyvista as pv
contact = fem.MultiPointContact(
    field=field,
    points=np.arange(mesh.npoints)[mesh.x == 1],
    centerpoint=-1,
    skip=(False, True, True)
)
plotter = pv.Plotter()
actor_1 = plotter.add_points(
    mesh.points[mpc.points],
    point_size=16,
    color="red",
)
actor_2 = plotter.add_points(
    mesh.points[[mpc.centerpoint]],
    point_size=16,
    color="green",
)
mesh.plot(plotter=contact.plot(plotter=plotter)).show()
