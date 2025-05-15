import felupe as fem
mesh = fem.Cube(n=6)
mesh.triangulate(mode=3).plot().show()
