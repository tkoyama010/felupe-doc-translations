left = fem.Boundary(displacement, fx=x.min(), value=-0.2)
left.update(-0.3)
left.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
