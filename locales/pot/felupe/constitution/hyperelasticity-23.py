import felupe as fem
umat = fem.Hyperelastic(fem.ogden, mu=[1, 0.2], alpha=[1.7, -1.5])
ax = umat.plot(incompressible=True)
