import felupe as fem
mesh = fem.Rectangle()
region = fem.RegionQuadBoundary(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Quad
##   Quadrature rule: GaussLegendreBoundary
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
