import felupe as fem
umat = fem.MaterialStrain(material=fem.linear_elastic, λ=2.0, μ=1.0)
ax = umat.plot()
