import felupe as fem
rect1 = fem.Rectangle(n=11)
rect2 = fem.Rectangle(a=(0.9, 0), b=(1.9, 1), n=11)
rect2
# Expected:
## <felupe Mesh object>
##   Number of points: 121
##   Number of cells:
##     quad: 100
