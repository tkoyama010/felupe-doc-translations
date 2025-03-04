right = fem.Boundary(displacement, fx=x.max())
right = fem.Boundary(displacement, fx=lambda x: np.isclose(x, x.max()))
right.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
