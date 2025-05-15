new_mask = np.logical_and(mask, y <= 0)
surface.apply_mask(new_mask)
surface.plot(color="red", plotter=mesh.plot(opacity=0.7)).show()
