# take some points from the inside for the fiber-reinforced area
eps = 1e-3
mask = np.arange(m.npoints)[np.logical_and.reduce([
    m.points[:, 0] >= 0.3,
    m.points[:, 0] <= 0.7 + eps,
    m.points[:, 1] >= 0.3,
    m.points[:, 1] <= 0.7 + eps,
])]

# copies of the mesh
mesh = [m.copy(), m.copy()]

# create sub-meshes (fiber, matrix)
mesh[0].update(cells=m.cells[ np.all(np.isin(m.cells, mask), axis=1)])
mesh[1].update(cells=m.cells[~np.all(np.isin(m.cells, mask), axis=1)])