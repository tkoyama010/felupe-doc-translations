import pyvista as pv
plotter = pv.Plotter()
actor = plotter.add_point_labels(
    points=np.pad(mesh.points, ((0, 0), (0, 1))),
    labels=[
        f"Point {i}: DOF {a}, {b}"
        for i, (a, b) in enumerate(displacement.indices.dof)
    ],
)
mesh.plot(plotter=plotter).show()
