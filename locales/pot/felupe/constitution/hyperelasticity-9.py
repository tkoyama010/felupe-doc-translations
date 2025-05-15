import felupe as fem
umat = fem.Hyperelastic(fem.arruda_boyce, C1=1.0, limit=3.2)
ax = umat.plot(incompressible=True)
