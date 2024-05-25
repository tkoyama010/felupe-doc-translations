import numpy as np
import felupe as fem

# math-functions which support trailing axes
from felupe.math import det, dya, identity, transpose, inv

class MyMaterialFormulation(fem.ConstitutiveMaterial):

    def __init__(self):
        # provide the shape of state variables without trailing axes
        # values are ignored - state variables are always initiated with zeros
        self.x = [np.zeros((3, 3))]

    def gradient(self, x):
        "Gradients of the strain energy density function."

        # extract variables
        F, p, statevars = x[0], x[1], x[-1]

        # user code
        dWdF = None  # first Piola-Kirchhoff stress tensor
        dWdp = None

        # update state variables
        # example: the displacement gradient
        statevars_new = F - identity(F)

        return [dWdF, dWdp, statevars_new]

    def hessian(self, x, **kwargs):
        "Hessians of the strain energy density function."

        # extract variables
        F, p, statevars = x[0], x[1], x[-1]

        # user code
        d2WdFdF = None  # fourth-order elasticity tensor
        d2WdFdp = None
        d2Wdpdp = None

        # upper-triangle items of the hessian
        return [d2WdFdF, d2WdFdp, d2Wdpdp]

umat = MyMaterialFormulation()