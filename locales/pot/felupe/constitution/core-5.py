import felupe as fem
umat = fem.LinearElastic(E=1, nu=0.3)
ax = umat.plot()
