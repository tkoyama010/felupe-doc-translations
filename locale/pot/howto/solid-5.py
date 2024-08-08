region_pressure = fem.RegionHexahedronBoundary(
    mesh=mesh,
    only_surface=True, # select only faces on the outline
    mask=mesh.points[:, 0] == 0, # select a subset of faces on the surface
)

field_boundary = fem.FieldContainer([fem.Field(region_pressure, dim=3)])
field_boundary.link(field)

body_pressure = fem.SolidBodyPressure(field=field_boundary)

force_pressure = body_pressure.assemble.vector(field=field_boundary, parallel=False)
stiffness_matrix_pressure = body_pressure.assemble.matrix(
    field=field_boundary, parallel=False
)