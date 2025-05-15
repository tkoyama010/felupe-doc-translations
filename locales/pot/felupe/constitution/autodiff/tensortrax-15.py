import felupe as fem
umat = fem.Hyperelastic(fem.anssari_benam_bucchi, mu=0.29, N=26.8)
ux = fem.math.linsteps([0.6, 5], num=50)
ps = fem.math.linsteps([1, 5], num=50)
bx = fem.math.linsteps([1, 3], num=50)
ax = umat.plot(ux=ux, ps=ps, bx=bx, incompressible=True)
