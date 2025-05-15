rectangle_quad4 = fem.Rectangle(n=6)
rectangle_quad8 = rectangle_quad4.convert(order=2)
rectangle_quad9 = fem.mesh.convert(rectangle_quad4, order=2, calc_midfaces=True)