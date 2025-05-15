axes_x = fem.Boundary(displacement, fx=0, fy=0, skip=(False, True))
axes_x.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
