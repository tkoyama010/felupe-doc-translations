regions = [
    fem.RegionTriangle(container.meshes[0]),
    fem.RegionQuad(container.meshes[1]),
]
fields = [
    fem.FieldContainer([fem.FieldPlaneStrain(regions[0], dim=2)]),
    fem.FieldContainer([fem.FieldPlaneStrain(regions[1], dim=2)]),
]