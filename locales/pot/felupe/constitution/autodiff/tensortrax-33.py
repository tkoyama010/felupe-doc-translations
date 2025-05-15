umat = mat.Hyperelastic(
    mat.models.hyperelastic.mooney_rivlin, C10=0.3, C01=0.8
)
ax = umat.plot(incompressible=True)
