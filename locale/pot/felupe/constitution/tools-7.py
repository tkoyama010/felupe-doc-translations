import felupe as fem
nh = fem.NeoHooke(mu=1.0)
vol = fem.Volumetric(bulk=2.0)
umat = nh & vol
ax = umat.plot()
