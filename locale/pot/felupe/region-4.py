import felupe as fem
mesh = fem.Cube()
region = fem.RegionHexahedron(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Hexahedron
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
##   Hessian evaluated: False
#
region.plot().show()
