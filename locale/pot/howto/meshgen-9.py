r = 25
R = 50
H = 100

rect = fem.Rectangle(a=(-r, 0), b=(-R, H), n=(11, 41))
cylinder = rect.revolve(n=19, phi=-180, axis=1)
cylinder.plot().show()