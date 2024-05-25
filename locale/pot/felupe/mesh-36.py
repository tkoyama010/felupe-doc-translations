import felupe as fem
mesh = fem.mesh.Triangle(a=(0.3, 0.2), b=(1.2, 0.1), c=(0.1, 0.9), n=3)
mesh.plot().show()
