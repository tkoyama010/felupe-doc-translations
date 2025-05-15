import felupe as fem
mesh = fem.Cube(n=3)
region = fem.RegionHexahedron(mesh)
region_dual = fem.RegionConstantHexahedron(mesh.dual(points_per_cell=1))
displacement = fem.Field(region, dim=3)
pressure = fem.Field(region_dual)
field = fem.FieldContainer([displacement, pressure])
field
# Expected:
## <felupe FieldContainer object>
##   Number of fields: 2
##   Dimension of fields:
##     Field: 3
##     Field: 1
