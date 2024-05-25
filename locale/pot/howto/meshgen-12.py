rectangle = fem.Rectangle(a=(-1, 0), b=(1, 5), n=(13, 26))
circle = fem.Circle(radius=1, centerpoint=(0, 5), sections=(0, 90), n=4)
triangle = fem.mesh.Triangle(a=(-1, 0), b=(1, 0), c=(0, -np.sqrt(12) / 2), n=7)
arm = fem.mesh.concatenate([rectangle, circle])

center = triangle.points.mean(axis=0)
arms = [arm.rotate(phi, axis=2, center=center) for phi in [0, 120, 240]]

mesh = fem.mesh.concatenate([triangle, *arms]).merge_duplicate_points(decimals=8)
mesh.plot().show()