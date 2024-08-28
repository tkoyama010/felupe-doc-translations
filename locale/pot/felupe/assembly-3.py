import numpy as np
import felupe as fem
mesh = fem.Rectangle()
region = fem.RegionQuad(mesh)
displacement = fem.Field(region, dim=2)
field = fem.FieldContainer([displacement])
bases = fem.assembly.expression.Basis(field)
len(bases[:])
1
#
bases[0].basis.shape
# Expected:
## (4, 2, 2, 4, 1)
#
bases[0].basis.grad.shape
# Expected:
## (4, 2, 2, 2, 4, 1)
#
bases[0].basis.hess.shape
# Expected:
## (4, 2, 2, 2, 2, 4, 1)
