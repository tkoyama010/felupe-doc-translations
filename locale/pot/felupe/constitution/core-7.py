import felupe as fem
umat = fem.LinearElasticLargeStrain(E=1.0, nu=0.3)
ax = umat.plot()
