from scipy.sparse import csr_matrix
import felupe as fem


class MyItem:
    def __init__(self, field):
        self.field = field
        self.assemble = fem.mechanics.Assemble(vector=self._vector, matrix=self._matrix)
        self.results = fem.mechanics.Results()

    def _vector(self, field=None, **kwargs):
        return csr_matrix(([0.0], ([0], [0])), shape=(1, 1))

    def _matrix(self, field=None, **kwargs):
        return csr_matrix(([0.0], ([0], [0])), shape=(1, 1))