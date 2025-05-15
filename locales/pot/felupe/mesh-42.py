import felupe as fem
mesh = fem.Rectangle(n=6)
mesh_with_midpoints_edges = fem.mesh.add_midpoints_edges(mesh)
mesh_with_midpoints_edges.plot(
    plotter=mesh.plot(), style="points", color="black"
).show()
