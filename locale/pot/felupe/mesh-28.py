import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
field = fem.FieldContainer([fem.Field(region, dim=3)])
new_points = mesh.rotate(angle_deg=-90, axis=2).points
mesh.update(points=new_points, callback=region.reload)
