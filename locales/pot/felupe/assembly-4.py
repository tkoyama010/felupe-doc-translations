import numpy as np
import felupe as fem
mesh = fem.Rectangle()
region = fem.RegionQuad(mesh)
displacement = fem.Field(region, dim=2)
bf = fem.assembly.expression.BasisField(displacement)
bf.basis.shape
# Expected:
## (4, 2, 2, 4, 1)
#
bf.basis.grad.shape
# Expected:
## (4, 2, 2, 2, 4, 1)
#
bf.basis.hess.shape
# Expected:
## (4, 2, 2, 2, 2, 4, 1)
