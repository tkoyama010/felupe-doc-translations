import numpy as np
import felupe as fem
mesh = fem.Rectangle(n=6)
region = fem.RegionQuad(mesh)
field = fem.FieldContainer([fem.FieldAxisymmetric(region, dim=2)])
boundaries = {"fixed": fem.Boundary(field[0], fx=0)}
solid = fem.SolidBody(umat=fem.NeoHooke(mu=1, bulk=2), field=field)
mask = np.logical_and(mesh.x == 1, mesh.y > 0.5)
region_stress = fem.RegionQuadBoundary(
    mesh=mesh,
    mask=mask,  # select a subset of faces on the surface
    ensure_3d=True,  # True for axisymmetric/plane strain
)
field_boundary = fem.FieldContainer([fem.FieldAxisymmetric(region_stress, dim=2)])
stress = fem.SolidBodyCauchyStress(field=field_boundary)
table = (
    fem.math.linsteps([0, 1], num=5, axis=1, axes=9)
    + fem.math.linsteps([0, 1], num=5, axis=3, axes=9)
).reshape(-1, 3, 3)
step = fem.Step(
    items=[solid, stress], ramp={stress: 1.0 * table}, boundaries=boundaries
)
job = fem.Job(steps=[step]).evaluate()
solid.plot("Principal Values of Cauchy Stress").show()
