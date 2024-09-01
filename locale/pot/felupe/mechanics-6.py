import felupe as fem
mesh = fem.mesh.Line(n=3)
element = fem.element.Line()
quadrature = fem.GaussLegendre(order=1, dim=1)
region = fem.Region(mesh, element, quadrature)
field = fem.FieldContainer([fem.Field(region, dim=1)])
load = fem.PointLoad(field, [1, 2], values=[[3], [5]])
vector = load.assemble.vector()
vector.toarray()
# Expected:
## array([[0.],
##        [3.],
##        [5.]])
