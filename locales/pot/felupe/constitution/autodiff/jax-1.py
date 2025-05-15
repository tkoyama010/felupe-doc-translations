import felupe as fem
import felupe.constitution.jax as mat
import jax.numpy as jnp
def neo_hooke(C, mu):
    "Strain energy function of the Neo-Hookean material formulation."
    return mu / 2 * (jnp.linalg.det(C) ** (-1/3) * jnp.trace(C) - 3)
umat = mat.Hyperelastic(neo_hooke, mu=1)
ax = umat.plot(incompressible=True)
