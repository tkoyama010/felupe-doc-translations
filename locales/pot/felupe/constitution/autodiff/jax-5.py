import felupe as fem
import felupe.constitution.jax as mat
import jax.numpy as jnp
def neo_hooke(F, mu):
    "First Piola-Kirchhoff stress of the Neo-Hookean material formulation."

    C = F.T @ F
    Cu = jnp.linalg.det(C) ** (-1/3) * C
    dev = lambda C: C - jnp.trace(C) / 3 * jnp.eye(3)

    return mu * F @ dev(Cu) @ jnp.linalg.inv(C)
umat = mat.Material(neo_hooke, mu=1)
ax = umat.plot(incompressible=True)
