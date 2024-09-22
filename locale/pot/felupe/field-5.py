from felupe.math import dot, transpose, eigvalsh, sqrt
F = displacement.extract(grad=True, add_identity=True)
C = dot(transpose(F), F)
λ = sqrt(eigvalsh(C))
