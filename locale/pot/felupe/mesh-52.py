mesh_new = fem.mesh.interpolate_line(mesh, xi=np.linspace(0, 1), axis=1)
mesh_new.plot(style="points", color="black").show()
