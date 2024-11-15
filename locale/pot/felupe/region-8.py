import felupe as fem
mesh = fem.mesh.Rectangle().triangulate()
region = fem.RegionTriangle(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Triangle
##   Quadrature rule: Triangle
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
