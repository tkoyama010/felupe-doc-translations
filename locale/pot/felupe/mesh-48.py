import felupe as fem
inner = fem.mesh.revolve(fem.Point(1)).expand(z=0.4).translate(0.2, axis=2)
outer = fem.mesh.revolve(fem.Point(2), phi=160).rotate(
    axis=2, angle_deg=20
).expand(z=1.2)
mesh = fem.mesh.fill_between(inner, outer, n=6)
mesh.plot().show()
