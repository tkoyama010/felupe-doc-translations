import felupe as fem

region = fem.RegionQuad(mesh=fem.Rectangle(b=(2, 1), n=(11, 6)))
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])

boundaries = fem.dof.uniaxial(field, clamped=True, move=-0.3, axis=1)[0]
solid = fem.SolidBody(umat=fem.NeoHooke(mu=1, bulk=5), field=field)

job = fem.Job(steps=[fem.Step(items=[solid], boundaries=boundaries)]).evaluate()