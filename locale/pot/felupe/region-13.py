import felupe as fem
mesh = fem.Rectangle().triangulate().add_midpoints_edges()
region = fem.RegionQuadraticTriangle(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: QuadraticTriangle
##   Quadrature rule: Triangle
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
