import numpy as np
import felupe as fem
from felupe.math import (
    cdya_ik,
    cdya_il,
    det,
    dya,
    identity,
    inv,
    transpose
)
def stress(x, mu, lmbda):
    F, statevars = x[0], x[-1]
    J = det(F)
    lnJ = np.log(J)
    iFT = transpose(inv(F, J))
    dWdF = mu * (F - iFT) + lmbda * lnJ * iFT
    return [dWdF, statevars]
def elasticity(x, mu, lmbda):
    F = x[0]
    J = det(F)
    iFT = transpose(inv(F, J))
    eye = identity(F)
    return [
        mu * cdya_ik(eye, eye) + lmbda * dya(iFT, iFT) +
        (mu - lmbda * np.log(J)) * cdya_il(iFT, iFT)
    ]
umat = fem.Material(stress, elasticity, mu=1.0, lmbda=2.0)
