import felupe as fem
cube = fem.Cube(a=(-3, -2, -1), b=(3, 2, 1), n=(31, 21, 11))
mesh = cube.add_runouts(axis=2, values=[0.1, 0.3], normalize=True)
mesh.plot().show()
