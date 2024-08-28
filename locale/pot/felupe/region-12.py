import felupe as fem
mesh = fem.Cube().triangulate().add_midpoints_edges()
region = fem.RegionQuadraticTetra(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: QuadraticTetra
##   Quadrature rule: Tetrahedron
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
