import felupe as fem
mesh = fem.Circle(sections=[0, 90, 180], n=5)
fem.mesh.mirror(mesh, normal=[0, 1, 0]).plot().show()
