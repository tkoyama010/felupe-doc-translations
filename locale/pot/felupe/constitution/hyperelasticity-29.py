import felupe as fem
umat = fem.Hyperelastic(
    fem.third_order_deformation, C10=0.5, C01=0.1, C11=0.01, C20=-0.1, C30=0.02
)
ax = umat.plot(incompressible=True)
