import felupe as fem
import numpy as np
class MyMaterialFormulation:
    def __init__(self, a=5):
        self.x = [np.zeros((3, 3))]
        self.kwargs = {"a": a}

    def gradient(self, x):
        F, statevars = x[0], x[-1]
        dWdF = self.kwargs["a"] * np.eye(3).reshape(3, 3, 1, 1)
        return [dWdF, statevars]

    def hessian(self, x, **kwargs):
        F, statevars = x[0], x[-1]
        d2WdFdF = self.kwargs["a"] * np.zeros((3, 3, 3, 3, 1, 1))
        return [d2WdFdF]
MyMaterial = fem.constitutive_material(MyMaterialFormulation)
umat = MyMaterial(a=0.5)
ax = umat.plot(incompressible=True)
