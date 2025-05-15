import felupe as fem
umat = fem.Hyperelastic(
    fem.lopez_pamies, mu=[0.2699,  0.00001771], alpha=[1.08, 4.40]
)
ux = fem.math.linsteps([0.6, 7], num=50)
ps = fem.math.linsteps([1, 7], num=50)
bx = fem.math.linsteps([1, 5], num=50)
ax = umat.plot(ux=ux, ps=ps, bx=bx, incompressible=True)
