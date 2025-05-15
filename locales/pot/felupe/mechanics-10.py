import felupe as fem
import numpy as np
mesh = fem.Rectangle(b=(5, 1), n=(50, 10))
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])
boundaries = dict(left=fem.Boundary(field[0], fx=0))
solid = fem.SolidBody(fem.LinearElastic(E=2.5, nu=0.25), field, density=1.0)
modal = fem.FreeVibration(items=[solid], boundaries=boundaries).evaluate()
eigenvector, frequency = modal.extract(n=4, inplace=True)
solid.plot("Stress", component=0).show()
