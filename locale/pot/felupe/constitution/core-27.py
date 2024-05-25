import felupe as fem
umat = fem.NeoHookeCompressible(mu=1.0, lmbda=2.0)
ax = umat.plot()
