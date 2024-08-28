import felupe as fem
cube = fem.Cube().add_midpoints_edges()
mesh = cube.add_midpoints_faces().add_midpoints_volumes()
region = fem.RegionTriQuadraticHexahedron(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: TriQuadraticHexahedron
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
