import felupe as fem
rect = fem.Rectangle(n=4)
cube = fem.mesh.expand(rect, n=7, z=2)
cube.plot().show()
