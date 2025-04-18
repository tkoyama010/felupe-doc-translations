import felupe as fem
import felupe.constitution.tensortrax as mat
import tensortrax.math as tm
def neo_hooke(C, mu):
    "Strain energy function of the Neo-Hookean material formulation."
    return mu / 2 * (tm.linalg.det(C) ** (-1/3) * tm.trace(C) - 3)
umat = mat.Hyperelastic(neo_hooke, mu=1)
ax = umat.plot(incompressible=True)
