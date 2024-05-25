import felupe as fem
mesh = fem.Rectangle(n=6)
mesh2 = fem.mesh.convert(mesh, order=2)
mesh2.plot(plotter=mesh.plot(), style="points", color="black").show()
