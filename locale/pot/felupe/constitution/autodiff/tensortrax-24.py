import felupe as fem
umat = fem.Hyperelastic(
    fem.finite_strain_viscoelastic, mu=1.0, eta=1.0, dtime=1.0, nstatevars=6
)
ax = umat.plot(
   incompressible=True,
   ux=fem.math.linsteps([1, 1.5, 1, 2, 1], num=[5, 5, 10, 10]),
   ps=None,
   bx=None,
)
