import felupe as fem
mesh = fem.Rectangle().add_midpoints_edges()
region = fem.RegionQuadraticQuad(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: QuadraticQuad
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
