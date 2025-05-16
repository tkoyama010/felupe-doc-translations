import felupe as fem
mesh = fem.Cube(n=3)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
field[0].values[mesh.x == 1, 0] += 0.5
field[0].values[mesh.x == 1, 2] += 0.5
field[0].values += mesh.rotate(-30, axis=1).points - mesh.points
face = fem.RegionHexahedronBoundary(mesh, mask=mesh.x == mesh.x.max())
u = fem.FieldContainer([fem.Field(face, dim=3)])
u.link(field)
mesh_faces = face.mesh_faces()
mesh_faces.points += field[0].values
C = fem.math.inplane(u.evaluate.right_cauchy_green_deformation(), face.tangents)
e = fem.math.strain(u, C=C, k=0)
view = mesh_faces.view(
    cell_data={"ep": fem.math.eigvalsh(e).max(axis=0).mean(axis=-2).T}
)
view.plot("ep", label="Strain (Max. Principal)", plotter=field.plot(style="wireframe")).show()
