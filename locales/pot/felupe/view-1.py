import numpy as np
import felupe as fem
scene = fem.view.Scene()
scene.mesh = fem.Cube(n=3).as_unstructured_grid()
scene.mesh.point_data["Displacement"] = np.arange(81).reshape(27, 3) / 300
scene.mesh.set_active_scalars(None)
scene.plot("Displacement", component=None).show()
