# a global and two sub-regions
region = fem.RegionQuad(m)
regions = [fem.RegionQuad(me) for me in mesh]

# a global and two sub-fields
field = fem.FieldContainer([fem.FieldPlaneStrain(region, dim=2)])
fields = [
    fem.FieldContainer([fem.FieldPlaneStrain(regions[0], dim=2)]),
    fem.FieldContainer([fem.FieldPlaneStrain(regions[1], dim=2)]),
]