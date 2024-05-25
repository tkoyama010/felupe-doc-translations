import felupe as fem
mesh = fem.Cube().add_midpoints_edges()
region = fem.RegionQuadraticHexahedron(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: QuadraticHexahedron
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
#
region.plot().show()
