import felupe as fem
mesh = fem.mesh.CubeArbitraryOrderHexahedron(order=3)
region = fem.RegionLagrange(mesh, order=3, dim=3)
region
# Expected:
## <felupe Region object>
##   Element formulation: ArbitraryOrderLagrange
##   Quadrature rule: GaussLegendre
##   Gradient evaluated: True
#
region.plot().show()
