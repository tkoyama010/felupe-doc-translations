mesh  = fem.Cube(n=5)
mesh_q2 = mesh.convert(
    order=2,
    calc_points=True,
    calc_midfaces=True,
    calc_midvolumes=True
)

region_q2 = fem.RegionTriQuadraticHexahedron(mesh_q2)
region_p1 = fem.RegionTetra(
    mesh=mesh.dual(points_per_cell=4),
    quadrature=region_q2.quadrature,
    grad=False
)

displacement = fem.Field(region_q2,  dim=3)
pressure     = fem.Field(region_p1, dim=1)
volumeratio  = fem.Field(region_p1, dim=1, values=1.0)

field = fem.FieldContainer(fields=[displacement, pressure, volumeratio])
solid = fem.SolidBody(umat=umat, field=field)