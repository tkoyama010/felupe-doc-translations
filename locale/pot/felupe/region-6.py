import felupe as fem
mesh = fem.Cube().triangulate()
region = fem.RegionTetra(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: Tetra
##   Quadrature rule: Tetrahedron
##   Gradient evaluated: True
#
region.plot().show()
