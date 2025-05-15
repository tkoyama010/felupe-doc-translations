import felupe.constitution.tensortrax as mat
import felupe as fem
r = fem.math.rotation_matrix(0, axis=2)
lmbda, mu = fem.constitution.lame_converter_orthotropic(
    E=[10, 10, 10],
    nu=[0.3, 0.3, 0.3],
    G=[1, 1, 1],
)
umat = mat.Hyperelastic(
    mat.models.hyperelastic.saint_venant_kirchhoff_orthotropic,
    mu=mu,
    lmbda=lmbda,
    r1=r[:, 0],
    r2=r[:, 1],
    r3=r[:, 2],
)
ax = umat.plot(ux=fem.math.linsteps([1, 1.1], num=10), ps=None, bx=None)
