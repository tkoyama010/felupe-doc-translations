umat = fem.NeoHooke(mu=1.0, bulk=2.0)
body = fem.SolidBody(umat=umat, field=field)

K = body.assemble.matrix() + mpc.assemble.matrix()
r = body.assemble.vector(field) + mpc.assemble.vector(field)

mesh.plot(plotter=mpc.plot()).show()