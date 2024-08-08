mesh = fem.Rectangle(a=(0, 30), b=(20, 40), n=(21, 11))
region = fem.RegionQuad(mesh)

region_pressure = fem.RegionQuadBoundary(
    mesh=mesh,
    only_surface=True, # select only faces on the outline
    mask=mesh.points[:, 0] == 0, # select a subset of faces on the surface
    ensure_3d=True, # flag for axisymmetric boundary region
)

field = fem.FieldContainer([fem.FieldAxisymmetric(region)])
field_boundary = fem.FieldContainer([fem.FieldAxisymmetric(region_pressure)])
field_boundary.link(field)