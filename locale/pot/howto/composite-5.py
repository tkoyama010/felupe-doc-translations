# two material model formulations
neo_hooke = fem.NeoHooke(mu=1, bulk=1)
linear_elastic = fem.LinearElasticLargeStrain(E=100, nu=0.3)

# the solid bodies
fiber = fem.SolidBody(umat=linear_elastic, field=fields[0])
matrix = fem.SolidBody(umat=neo_hooke, field=fields[1])