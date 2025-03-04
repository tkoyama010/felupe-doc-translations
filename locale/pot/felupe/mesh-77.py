import felupe as fem
mesh = fem.Cube(n=6)
triangulated = fem.mesh.triangulate(mesh, mode=3)
triangulated.plot().show()
