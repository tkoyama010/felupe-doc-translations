import felupe as fem
mesh = fem.Cube(n=6)
region = fem.RegionHexahedron(mesh)
displacement = fem.Field(region, dim=3)
pressure = fem.FieldDual(region)
field = fem.FieldContainer([displacement, pressure])
field
# Expected:
## <felupe FieldContainer object>
##   Number of fields: 2
##   Dimension of fields:
##     Field: 3
##     FieldDual: 1
