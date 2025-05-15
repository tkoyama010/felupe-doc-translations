import numpy as np
import felupe as fem
mesh = fem.Cube(n=3)
displacement = np.arange(81).reshape(27, 3) / 300
view = fem.ViewMesh(mesh, point_data={"Displacement": displacement})
view.plot("Displacement", component=None).show()
