import felupe as fem
mesh = fem.Rectangle(n=6)
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldAxisymmetric(region, dim=2)])
boundaries = fem.dof.symmetry(field[0])
umat = fem.NeoHooke(mu=1, bulk=2)
solid = fem.SolidBody(umat, field)
region_pressure = fem.RegionQuadBoundary(
    mesh=mesh,
    only_surface=True,  # select only faces on the outline
    mask=mesh.points[:, 0] == 1,  # select a subset of faces on the surface
    ensure_3d=True,  # requires True for axisymmetric/plane strain, otherwise False
)
field_boundary = fem.FieldContainer([fem.FieldAxisymmetric(region_pressure, dim=2)])
pressure = fem.SolidBodyPressure(field=field_boundary)
table = fem.math.linsteps([0, 1], num=5)
step = fem.Step(
    items=[solid, pressure], ramp={pressure: 1 * table}, boundaries=boundaries
)
job = fem.Job(steps=[step]).evaluate()
solid.plot(
    "Principal Values of Cauchy Stress", component=2, clim=[-1.01, -0.99]
).show()
