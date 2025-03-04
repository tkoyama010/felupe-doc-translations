import felupe as fem
import numpy as np
from scipy.interpolate import CubicSpline
mesh = fem.mesh.Line(b=1.0, n=5).expand(n=1)
t = mesh.x.copy()
mesh.points[:, 0] = np.sin(2 * np.pi * t)
mesh.points[:, 1] = np.cos(2 * np.pi * t)
mesh_new = fem.mesh.interpolate_line(
    mesh, xi=np.linspace(0, 1), Interpolator=CubicSpline, bc_type="periodic"
)
mesh_new.plot(
    plotter=mesh.plot(style="points", color="red", point_size=15),
    color="black",
).show()
