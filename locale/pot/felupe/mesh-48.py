import felupe as fem
mesh = fem.Rectangle(n=5).add_midpoints_edges()
region = fem.RegionQuadraticQuad(mesh=mesh)
mesh_dual = fem.mesh.dual(mesh, points_per_cell=1, disconnect=False)
region_dual = fem.RegionConstantQuad(
    mesh_dual, quadrature=region.quadrature, grad=False
)
displacement = fem.FieldPlaneStrain(region, dim=2)
pressure = fem.Field(region_dual)
field = fem.FieldContainer([displacement, pressure])
