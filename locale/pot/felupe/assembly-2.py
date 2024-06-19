from felupe.math import ddot, trace, sym, grad
@fem.Form(v=field, u=field, kwargs={"μ": 1.0, "λ": 2.0})
def bilinearform():
    "A container for a bilinear form."

    def linear_elasticity(v, u, μ, λ):
        "Linear elasticity."

        δε, ε = sym(grad(v)), sym(grad(u))
        return 2 * μ * ddot(δε, ε) + λ * trace(δε) * trace(ε)

    return [linear_elasticity]
stiffness_matrix = bilinearform.assemble(v=field, u=field, parallel=False)
system = fem.solve.partition(
    field, stiffness_matrix, dof1=loadcase["dof1"], dof0=loadcase["dof0"]
)
field += fem.solve.solve(*system, ext0=loadcase["ext0"])
field.plot("Principal Values of Logarithmic Strain").show()
