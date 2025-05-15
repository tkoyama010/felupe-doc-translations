import felupe as fem

neohooke = fem.constitution.NeoHooke(mu=1.0, bulk=5000.0)
umat = fem.constitution.ThreeFieldVariation(neohooke)