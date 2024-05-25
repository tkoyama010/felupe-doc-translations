import felupe as fem
mesh = fem.Cube()
region = fem.RegionHexahedronBoundary(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Hexahedron
##   Quadrature rule: GaussLegendreBoundary
##   Gradient evaluated: True
#
region.plot().show()
