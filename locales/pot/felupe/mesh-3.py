import felupe as fem
mesh = fem.Rectangle(n=6)
mesh_with_midpoints_faces = mesh.add_midpoints_faces(cell_type="quad")
mesh_with_midpoints_faces.plot(
    plotter=mesh.plot(), style="points", color="black"
).show()
