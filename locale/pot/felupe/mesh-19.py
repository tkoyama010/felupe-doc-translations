mesh = stack.merge_duplicate_points()
mesh
# Expected:
## <felupe Mesh object>
##   Number of points: 220
##   Number of cells:
##     quad: 200
#
mesh.plot(opacity=0.6).show()
