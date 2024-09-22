import felupe as fem
mesh = fem.Rectangle(n=4)
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])
evaluate = fem.field.EvaluateFieldContainer(field)
F = evaluate.deformation_gradient()
F.shape  # (3, 3, nquadraturepoints, ncells)
# Expected:
## (3, 3, 4, 9)
#
F[..., 0, 0]  # deformation gradient of first cell, first quadrature point
# Expected:
## array([[1., 0., 0.],
##        [0., 1., 0.],
##        [0., 0., 1.]])
