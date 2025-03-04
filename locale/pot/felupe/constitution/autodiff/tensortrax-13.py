import felupe as fem
umat = fem.Hyperelastic(
   fem.alexander, C1=17, C2=19.85, C3=1, gamma=0.735, k=0.00015
)
ux = fem.math.linsteps([0.6, 5], num=50)
ps = fem.math.linsteps([1, 5], num=50)
bx = fem.math.linsteps([1, 3], num=50)
ax = umat.plot(ux=ux, ps=ps, bx=bx, incompressible=True)
