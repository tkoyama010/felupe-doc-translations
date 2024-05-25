import felupe as fem
rect = fem.Rectangle(a=(-3, -1), b=(3, 1), n=(31, 11))
mesh = rect.add_runouts(axis=1, values=[0.2], normalize=True)
mesh.plot().show()
