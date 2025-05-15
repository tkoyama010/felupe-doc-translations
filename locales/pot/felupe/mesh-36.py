import felupe as fem
mesh = fem.mesh.Cube(a=(-1.2, 0.5, 6.2), b=(4.5, 7.3, 9.3), n=(3, 2, 2))
mesh.plot().show()
