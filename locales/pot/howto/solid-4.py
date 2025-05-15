body = fem.SolidBodyForce(field=field, values=[9810, 0, 0], scale=7.85e-9)

force_gravity = body.assemble.vector(field, parallel=False)