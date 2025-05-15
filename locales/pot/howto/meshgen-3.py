vert = fem.Point(a=1)
line = vert.expand(n=7, z=2)
rect = line.expand(n=5, z=5)
cube = rect.expand(n=6, z=3)

cube.plot().show()