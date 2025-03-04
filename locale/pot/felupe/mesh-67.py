import felupe as fem
rect = fem.Rectangle(b=(3, 1), n=(10, 4))
mesh = fem.mesh.rotate(rect, angle_deg=35, axis=2, center=[1.5, 0.5])
mesh.plot().show()
