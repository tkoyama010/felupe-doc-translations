n = (11, 9)
phi = np.linspace(1, 0.5, n[0]) * np.pi / 2

line = fem.mesh.Line(n=n[0])
bottom = line.copy(points=0.5 * np.vstack([np.cos(phi), np.sin(phi)]).T)
top = line.copy(
    points=np.vstack([np.linspace(0, 1, n[0]), np.linspace(1, 1, n[0])]).T
)

face = bottom.fill_between(top, n=n[1])
plate_with_hole = fem.mesh.concatenate(
    [face, face.mirror(normal=[-1, 1, 0])]
).merge_duplicate_points()

plate_with_hole.plot().show()