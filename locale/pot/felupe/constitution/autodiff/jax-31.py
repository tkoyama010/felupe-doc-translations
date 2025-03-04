import felupe as fem
umat = mat.Hyperelastic(
    mat.models.hyperelastic.van_der_waals,
    mu=1.0,
    beta=0.1,
    a=0.5,
    limit=5.0
)
ax = umat.plot(incompressible=True)
