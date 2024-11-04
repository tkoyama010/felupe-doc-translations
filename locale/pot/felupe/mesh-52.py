import felupe as fem
import numpy as np
mesh = fem.mesh.Line(n=5).expand(n=1)
t = mesh.x.copy()
mesh.points[:, 0] = np.sin(np.pi / 2 * t)
mesh.points[:, 1] = np.cos(np.pi / 2 * t)
mesh.plot(style="points", color="black").show()
