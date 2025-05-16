# import pyvista as pv

# plotter = pv.Plotter(shape=(2, 2))
# kwargs = dict(name="Cauchy Stress", component=1, plotter=plotter)

# plotter.subplot(0, 0)
# kwargs_sbar = dict(interactive=False, title="Cauchy Stress YY (None)")
# solid.plot(project=None, **kwargs, scalar_bar_args=kwargs_sbar)

# plotter.subplot(0, 1)
# kwargs_sbar = dict(interactive=False, title="Cauchy Stress YY (topoints)")
# solid.plot(project=fem.topoints, **kwargs, scalar_bar_args=kwargs_sbar)

# plotter.subplot(1, 0)
# kwargs_sbar = dict(interactive=False, title="Cauchy Stress YY (project)")
# solid.plot(project=fem.project, **kwargs, scalar_bar_args=kwargs_sbar)

# plotter.subplot(1, 1)
# kwargs_sbar = dict(interactive=False, title="Cauchy Stress YY (extrapolate)")
# solid.plot(project=fem.tools.extrapolate, **kwargs, scalar_bar_args=kwargs_sbar)

# plotter.show()