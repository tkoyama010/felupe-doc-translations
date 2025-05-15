import felupe as fem
rect1 = fem.Rectangle(n=11)
rect2 = fem.Rectangle(a=(0.9, 0), b=(1.9, 1), n=11)
container = fem.MeshContainer([rect1, rect2])
stack = fem.mesh.stack(container.meshes)
mesh = fem.mesh.merge_duplicate_points(stack)
mesh.plot(opacity=0.6).show()
