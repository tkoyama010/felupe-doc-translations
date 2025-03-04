container = fem.MeshContainer([inner, outer], merge=True)
field = fem.Field.from_mesh_container(container).as_container()

field.plot(plotter=container.plot(), point_size=15, color="red").show()