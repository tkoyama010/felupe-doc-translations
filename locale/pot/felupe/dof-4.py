center = fem.Boundary(displacement, fx=0, fy=0, mode="and")
center.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
