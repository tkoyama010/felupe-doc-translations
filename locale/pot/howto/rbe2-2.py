mpc = fem.MultiPointConstraint(
    field=field,
    points=np.arange(mesh.npoints)[mesh.points[:, 0] == 1],
    centerpoint=mesh.npoints - 1,
    skip=(0,1,1),
)