import felupe as fem
mesh = fem.Rectangle(n=11)
rect1, rect2 = mesh.copy(), mesh.copy()
rect1.update(cells=mesh.cells[: 40])
rect2.update(cells=mesh.cells[-50:])
container = fem.MeshContainer([rect1, rect2])
mesh = container.stack()
mesh.plot().show()
