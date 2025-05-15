import felupe as fem
import pyvista as pv
grid = pv.UnstructuredGrid(pv.examples.hexbeamfile)
container = fem.MechContainer.from_unstructured_grid(grid)
container
# Expected:
## <felupe mesh container object>
##   Number of points: 99
##   Number of cells:
##     hexahedron: 40
