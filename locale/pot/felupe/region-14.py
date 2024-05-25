import felupe as fem
mesh = fem.Cube().triangulate().add_midpoints_volumes()
region = fem.RegionTetraMINI(mesh)
region
# Expected:
## <felupe Region object>
##   Element formulation: TetraMINI
##   Quadrature rule: Tetrahedron
##   Gradient evaluated: True
#
region.plot().show()
