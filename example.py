import code.scheMC as scheMC

schematic = scheMC.Schematic()
schematic.placeblock((0, 0, 0), 'minecraft:lime_stained_glass')
schematic.placeblock((0, 1, 2), 'minecraft:emerald_block')
schematic.placeblock((1, 2, 3), 'minecraft:diamond_block')
schematic.save('example.schem')