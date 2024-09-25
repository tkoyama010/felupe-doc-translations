umat = fem.NeoHooke(mu=1)
solid = fem.SolidBodyNearlyIncompressible(umat, field, bulk=5000)