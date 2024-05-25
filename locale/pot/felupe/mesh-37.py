import felupe as fem
mesh = fem.mesh.RectangleArbitraryOrderQuad(order=5).add_runouts()
mesh.plot(nonlinear_subdivision=4).show()
