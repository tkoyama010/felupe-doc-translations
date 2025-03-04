import felupe as fem
umat = fem.LinearElasticOrthotropic(
    E=[1, 1, 1], nu=[0.3, 0.3, 0.3], G=[0.4, 0.4, 0.4]
)
ax = umat.plot()
