region = fem.RegionHexahedron(mesh=fem.Cube(n=3))
field = fem.FieldContainer([fem.Field(region, dim=3)])
boundaries, loadcase = fem.dof.uniaxial(field, clamped=True, move=1.0)

solid = fem.SolidBody(umat=fem.NeoHooke(mu=1, bulk=2), field=field)
my_item = MyItem(field=field)

step = fem.Step(items=[solid, my_item], boundaries=boundaries)
job = fem.Job(steps=[step]).evaluate()