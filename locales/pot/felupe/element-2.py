import felupe as fem
import tensortrax as tr
import numpy as np
class Hexahedron(fem.Element):
    def __init__(self):
        a = [-1, 1, 1, -1, -1, 1, 1, -1]
        b = [-1, -1, 1, 1, -1, -1, 1, 1]
        c = [-1, -1, -1, -1, 1, 1, 1, 1]
        self.points = np.vstack([a, b, c]).T

        # additional attributes for plotting, optional
        self.cells = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])
        self.cell_type = "hexahedron"

    def fun(self, rst):
        a, b, c = tr.math.array(self.points.T, shape=(3, 8), like=rst)
        r, s, t = rst
        ar, bs, ct = 1 + a * r, 1 + b * s, 1 + c * t
        return (ar * bs * ct) / 8

    def function(self, rst):
        return tr.function(self.fun)(rst)

    def gradient(self, rst):
        return tr.jacobian(self.fun)(rst)

    def hessian(self, rst):
        return tr.hessian(self.fun)(rst)
mesh = fem.Cube(n=6)
element = Hexahedron()
quadrature = fem.GaussLegendre(order=1, dim=3)
region = fem.Region(mesh, element, quadrature, hess=True)
