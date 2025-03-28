import mcschematic
import os
import sys

def save_schematic():

    file_name = 'new2'

    current_directory = os.path.dirname(sys.argv[0])
    schematic.save(current_directory, file_name, mcschematic.Version.JE_1_20_1)
    print(f"File saved: {os.path.join(current_directory, file_name)}]")

schematic = mcschematic.MCSchematic()
schematic.setBlock((0, 0, 0), "minecraft:lime_stained_glass")
schematic.setBlock((1, 1, 1), "minecraft:red_stained_glass")
save_schematic()