import felupe as fem
umat = fem.MaterialStrain(
    material=fem.linear_elastic_plastic_isotropic_hardening,
    λ=2.0,
    μ=1.0,
    σy=0.05,
    K=0.1,
    dim=3,
    statevars=(1, (3, 3)),
)
ux = fem.math.linsteps([1, 1.05, 0.95, 1.05], num=[10, 20, 20])
ax = umat.plot(ux=ux, bx=None, ps=None)
