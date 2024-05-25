import felupe as fem
import matadi as mat
MaterialHyperelastic = fem.constitutive_material(mat.MaterialHyperelastic)
umat = MaterialHyperelastic(mat.models.neo_hooke, C10=0.5)
ax = umat.plot(incompressible=True)
