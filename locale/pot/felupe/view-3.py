import numpy as np
import felupe as fem
mesh = fem.Cube(n=3)
region = fem.RegionHexahedron(mesh)
u = np.sqrt(1 + np.arange(81)).reshape(27, 3) / 100
field = fem.FieldContainer([fem.Field(region, values=u)])
view = fem.ViewField(field, project=fem.project)
view.plot("Principal Values of Logarithmic Strain").show()
