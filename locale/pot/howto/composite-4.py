boundaries = dict(
    fixed=fem.Boundary(field[0], fx=0),
    move=fem.Boundary(field[0], fx=1),
)