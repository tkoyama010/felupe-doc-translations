import felupe as fem
umat = mat.Hyperelastic(
    mat.models.hyperelastic.miehe_goektepe_lulei,
    mu=0.1475,
    N=3.273,
    p=9.31,
    U=9.94,
    q=0.567,
)
ux = ps = fem.math.linsteps([1, 2], num=50)
bx = fem.math.linsteps([1, 1.5], num=50)
ax = umat.plot(ux=ux, ps=ps, bx=bx, incompressible=True)
