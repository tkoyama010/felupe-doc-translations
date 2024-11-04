import felupe as fem
cube = fem.Cube(n=3)
cylinder = fem.Circle().expand(n=2)
mesh = fem.MeshContainer([cube, cylinder], merge=True)
mesh.plot().show()
