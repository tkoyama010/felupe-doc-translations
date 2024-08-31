import felupe as fem
umat = fem.LinearElasticOrthotropic(
    E1=1, E2=1, E3=1, nu12=0.3, nu23=0.3, nu13=0.3, G12=0.4, G23=0.4, G13=0.4
)
ax = umat.plot()
