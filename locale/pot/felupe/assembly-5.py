import numpy as np
import felupe as fem
x = fem.assembly.expression.BasisArray(
    np.ones(3), grad=np.zeros((3, 3)), hess=np.zeros((3, 3, 3))
)
x
# Expected:
## BasisArray([1., 1., 1.])
#
x.grad
# Expected:
## array([[0., 0., 0.],
##        [0., 0., 0.],
##        [0., 0., 0.]])
#
x.hess
# Expected:
## array([[[0., 0., 0.],
##         [0., 0., 0.],
##         [0., 0., 0.]],
#
#        [[0., 0., 0.],
#         [0., 0., 0.],
#         [0., 0., 0.]],
#
#        [[0., 0., 0.],
#         [0., 0., 0.],
