umat = mat.Hyperelastic(
    mat.models.hyperelastic.yeoh, C10=0.5, C20=-0.1, C30=0.02
)
ax = umat.plot(incompressible=True)
