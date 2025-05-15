mask = np.logical_and(np.isclose(x**2 + y**2, 1), x >= 0)
surface = fem.Boundary(displacement, mask=mask)
surface.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
