import felupe as fem
rect = fem.Rectangle()
mesh = rect.add_midpoints_edges().add_midpoints_faces()
region = fem.RegionBiQuadraticQuad(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: BiQuadraticQuad
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
