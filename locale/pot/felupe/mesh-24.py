import felupe as fem
rect = fem.Rectangle(a=(0, 4), b=(3, 5), n=(10, 4))
mesh = rect.revolve(n=11, phi=180, axis=0)
mesh.plot().show()
