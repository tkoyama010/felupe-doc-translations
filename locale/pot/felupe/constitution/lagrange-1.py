import felupe as fem
import tensortrax.math as tm
def neo_hooke(F, mu):
    C = tm.dot(tm.transpose(F), F)
    S = mu * tm.special.dev(tm.linalg.det(C)**(-1/3) * C) @ tm.linalg.inv(C)
    return F @ S
umat = fem.MaterialAD(neo_hooke, mu=1)
ax = umat.plot(incompressible=True)
