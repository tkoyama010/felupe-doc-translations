import felupe as fem
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

    def function(self, rst):
        r, s, t = rst
        a, b, c = self.points.T
        ar, bs, ct = 1 + a * r, 1 + b * s, 1 + c * t
        return (ar * bs * ct) / 8

    def gradient(self, rst):
        r, s, t = rst
        a, b, c = self.points.T
        ar, bs, ct = 1 + a * r, 1 + b * s, 1 + c * t
        return np.stack([a * bs * ct, ar * b * ct, ar * bs * c], axis=1)
mesh = fem.Cube(n=6)
element = Hexahedron()
quadrature = fem.GaussLegendre(order=1, dim=3)
region = fem.Region(mesh, element, quadrature)
