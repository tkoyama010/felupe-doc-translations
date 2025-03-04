import felupe as fem
umat = mat.Hyperelastic(mat.models.hyperelastic.neo_hooke, mu=1.0)
ax = umat.plot(incompressible=True)
