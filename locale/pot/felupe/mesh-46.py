mesh_new = interpolate_line(mesh, xi=np.linspace(0, 1, 101), axis=1)
mesh_new.plot(style="points", color="black").show()
