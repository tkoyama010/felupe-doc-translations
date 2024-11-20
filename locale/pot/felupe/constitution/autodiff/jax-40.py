umat = mat.Material(
    mat.models.lagrange.morph_representative_directions,
    p=[0.011, 0.408, 0.421, 6.85, 0.0056, 5.54, 5.84, 0.117],
    nstatevars=84,
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
