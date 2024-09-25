job = fem.CharacteristicCurve(steps=[step], boundary=boundaries["move"])
job.evaluate(filename="result.xdmf")

fig, ax = job.plot(
    xlabel=r"Displacement $d_1$ in mm $\longrightarrow$",
    ylabel=r"Normal Force $F_1$ in N $\longrightarrow$",
)