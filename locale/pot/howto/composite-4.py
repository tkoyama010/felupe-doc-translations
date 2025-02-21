boundaries = dict(
    fixed=fem.Boundary(field[0], fx=field.region.mesh.x.min()),
    move=fem.Boundary(field[0], fx=field.region.mesh.x.max()),
)