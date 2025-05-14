displacement & pressure
# Expected:
## <felupe FieldContainer object>
##   Number of fields: 2
##   Dimension of fields:
##     Field: 3
##     Field: 1
#
volume_ratio = fem.Field(region_dual)
field & volume_ratio  # displacement & pressure & volume_ratio
# Expected:
## <felupe FieldContainer object>
##   Number of fields: 3
##   Dimension of fields:
##     Field: 3
##     Field: 1
##     Field: 1
