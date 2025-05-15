import pyvista as pv
cell_types_pyvista_to_felupe = dict(cell_types_array[:, [1, 0]])
cell_types_pyvista_to_felupe[pv.CellType.LINE]
# Expected:
## "line"
