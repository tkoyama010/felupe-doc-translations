import felupe as fem
umat = fem.Hyperelastic(fem.neo_hooke, mu=1.0)
ax = umat.plot(incompressible=True)
