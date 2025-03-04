import felupe as fem
mesh = fem.Rectangle()
region = fem.RegionQuad(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Quad
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
