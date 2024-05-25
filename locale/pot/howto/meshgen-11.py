x = np.linspace(0, 1, 11)
y = np.linspace(0, 1, 11)

xg, yg = np.meshgrid(x, y, indexing="ij")
zg = (
    0.5 + 0.3 * xg**2 + 0.5 * yg**2 - 0.7 * yg ** 3 + np.random.rand(11, 11) / 50
)

grid = fem.Grid(x, y)
top = grid.copy(points=np.hstack([grid.points, zg.reshape(-1, 1)]))
bottom = grid.copy(points=np.hstack([grid.points, 0 * zg.reshape(-1, 1)]))

bottom.points += [0.2, 0.1, 0]
bottom.points *= 0.75

mesh = bottom.fill_between(top, n=6)
mesh.plot().show()