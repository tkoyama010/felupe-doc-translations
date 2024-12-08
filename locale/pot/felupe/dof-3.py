axes = fem.Boundary(displacement, fx=0, fy=0, mode="or")
axes.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
