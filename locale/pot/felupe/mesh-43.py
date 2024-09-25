import felupe as fem
import pyvista as pv
mesh = fem.Cube(n=6)
mesh_with_midpoints_volumes = fem.mesh.add_midpoints_volumes(
    mesh, cell_type_new="hexahedron9"
)
plotter = pv.Plotter()
actor = plotter.add_points(mesh_with_midpoints_volumes.points, color="black")
mesh.plot(opacity=0.5, plotter=plotter).show()
