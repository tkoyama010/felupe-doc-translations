umat = mat.Material(
    mat.models.lagrange.morph,
    p=[0.039, 0.371, 0.174, 2.41, 0.0094, 6.84, 5.65, 0.244],
    nstatevars=13,
)
ax = umat.plot(
   incompressible=True,
   ux=fem.math.linsteps(
       # [1, 2, 1, 2.75, 1, 3.5, 1, 4.2, 1, 4.8, 1, 4.8, 1],
       [1, 2.75, 1, 2.75],
       num=20,
   ),
   ps=None,
   bx=None,
)
