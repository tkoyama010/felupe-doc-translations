block = plate_with_hole.expand(z=0.5)
x, y, z = block.points.T

solid = block.add_runouts(
    centerpoint=[0, 0, 0],
    axis=2,
    values=[0.07, 0.02],
    exponent=5,  # shape parameter
    normalize=True,
    mask=np.arange(block.npoints)[np.sqrt(x**2 + y**2) > 0.5]
)
solid.plot().show()