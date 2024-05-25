import numpy as np
import felupe as fem
mesh = fem.Rectangle(b=(3, 1), n=(16, 6))
mesh.plot().show()
