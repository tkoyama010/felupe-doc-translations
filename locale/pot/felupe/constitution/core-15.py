import felupe as fem
umat = fem.constitution.LinearElasticTensorNotation(E=1, nu=0.3)
ax = umat.plot()
