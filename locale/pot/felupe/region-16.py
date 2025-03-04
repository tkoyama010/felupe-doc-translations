import felupe as fem
mesh = fem.Rectangle().triangulate().add_midpoints_faces()
region = fem.RegionTriangleMINI(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: TriangleMINI
##   Quadrature rule: Triangle
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
