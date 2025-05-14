circle = fem.Circle(radius=1, centerpoint=(0, 0), sections=(0, 90, 180, 270), n=6)

phi = np.linspace(1, 0.5, 6) * np.pi / 2

line = fem.mesh.Line(n=6)
curve = line.copy(points=1.0 * np.vstack([np.cos(phi), np.sin(phi)]).T)
top = line.copy(points=np.vstack([np.linspace(0, 1.5, 6), np.linspace(1.5, 1.5, 6)]).T)

transition = curve.fill_between(top, n=6)
transition = fem.mesh.concatenate([transition, transition.mirror(normal=[-1, 1, 0])])

rect = fem.Rectangle(a=(-1.5, 1.5), b=(1.5, 5.0), n=(11, 14))
rect.points[:, 0] *= 1 + (rect.points[:, 1] - 1.5) / 10

face = fem.mesh.concatenate([
    transition,
    transition.mirror(normal=[1, 0, 0]),
    fem.mesh.Line(a=-1.5, b=-1, n=6).revolve(n=21, phi=180, axis=2).flip(),
    rect
])

mesh = fem.mesh.concatenate([
    face.expand(n=6, z=0.5),
    circle.expand(n=11, z=1),
]).merge_duplicate_points(decimals=8)

mesh.plot().show()