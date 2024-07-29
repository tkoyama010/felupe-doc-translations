import numpy as np
import felupe as fem
λ, P = np.array(
    [
        [1.000, 0.00],
        [1.240, 2.30],
        [1.585, 4.16],
        [2.180, 6.00],
        [3.020, 8.80],
        [4.030, 12.5],
        [4.760, 16.2],
        [5.750, 23.6],
        [6.850, 38.5],
        [7.250, 49.6],
        [7.600, 64.4],
    ]
).T * np.array([[1.0], [0.0980665]])
umat = fem.Hyperelastic(fem.anssari_benam_bucchi)
umat_new, res = umat.optimize(
    ux=[λ, P], incompressible=True, relative=True
)
ux = np.linspace(λ.min(), λ.max(), num=50)
ax = umat_new.plot(incompressible=True, ux=ux, bx=None, ps=None)
ax.plot(λ, P, "C0x")
