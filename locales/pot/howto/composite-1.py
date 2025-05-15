import felupe as fem

inner = fem.Rectangle(a=(-1, -1), b=(1, 1), n=(5, 5)).triangulate()

lower = fem.Rectangle(a=(-3, -3), b=(3, -1), n=(13, 5))
upper = fem.Rectangle(a=(-3, 1), b=(3, 3), n=(13, 5))
left = fem.Rectangle(a=(-3, -1), b=(-1, 1), n=(5, 5))
right = fem.Rectangle(a=(1, -1), b=(3, 1), n=(5, 5))

outer = fem.MeshContainer([lower, upper, left, right], merge=True).stack()

container = fem.MeshContainer([inner, outer], merge=True)