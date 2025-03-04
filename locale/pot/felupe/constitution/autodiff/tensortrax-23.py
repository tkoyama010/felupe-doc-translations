import felupe as fem
umat = mat.Hyperelastic(
    mat.models.hyperelastic.extended_tube,
    Gc=0.1867,
    Ge=0.2169,
    beta=0.2,
    delta=0.09693,
)
ax = umat.plot(incompressible=True)
