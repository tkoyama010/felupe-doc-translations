import felupe as fem
umat = fem.Hyperelastic(fem.extended_tube, Gc=0.2, Ge=0.2, beta=0.2, delta=0.1)
preview = fem.ViewMaterialIncompressible(umat)
ax = preview.plot(show_title=True, show_kwargs=True)
