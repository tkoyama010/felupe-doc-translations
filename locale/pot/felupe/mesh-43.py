import felupe as fem
mesh = fem.Rectangle(n=6)
mesh_with_midpoints_faces = fem.mesh.add_midpoints_faces(
    mesh, cell_type_new="quad"
)
plotter = mesh_with_midpoints_faces.plot(
    plotter=mesh.plot(), style="points", color="black"
).show()
