import felupe as fem
umat = fem.Hyperelastic(fem.saint_venant_kirchhoff, mu=1.0, lmbda=20.0)
ax = umat.plot(incompressible=False)
