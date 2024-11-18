import felupe as fem
umat = mat.Hyperelastic(mat.models.hyperelastic.blatz_ko, mu=1.0)
ax = umat.plot()
