import felupe as fem
mesh = fem.Point(a=-2.1)
mesh
# Expected:
## <felupe Mesh object>
##   Number of points: 1
##   Number of cells:
##     vertex: 1
#
mesh.points
# Expected:
## array([[-2.1]])
#
mesh.cells
# Expected:
## array([[0]])
