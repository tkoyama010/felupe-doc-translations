import felupe as fem
import pyvista as pv
plotter = pv.Plotter()
sphere = pv.Sphere(radius=1).clip(normal="z", invert=False)
actor = plotter.add_mesh(sphere, opacity=0.3, color="white")
quadrature = fem.BazantOh(n=21)
quadrature.plot(plotter=plotter, weighted=True).show()
