from code.write import create_file

class Schematic():

    def __init__(self):
        self.placements = {}

    def placeblock(self, position, block_name):
        self.placements[position] = block_name

    def save(self, file_name, base_block='minecraft:air'):
        if self.placements:
            min_pos = list(map(min, zip(*self.placements)))
            max_pos = list(map(max, zip(*self.placements)))
        else:
            min_pos = [0] * 3
            max_pos = [0] * 3

        self.placements = {
            tuple(axis - min_pos[j] for j, axis in enumerate(position)): block
            for position, block in self.placements.items()
        }
        max_pos = [axis - min_pos[i] + 1 for i, axis in enumerate(max_pos)]

        block_set = set(self.placements.values())
        block_dict_ids = {value: index + 1 for index, value in enumerate(block_set)}

        block_list_final = [0]*max_pos[0]*max_pos[1]*max_pos[2]

        for key, value in self.placements.items(): #(Y*Z_max + Z)*X_max + X
            index = (key[1]*max_pos[2] + key[2])*max_pos[0] + key[0]
            block_list_final[index] = block_dict_ids[value]

        palette = ['Palette'] + [[3, base_block, 0]] + [[3, key, value] for key, value in block_dict_ids.items()] + [[0, None, None]]

        create_file(file_name, max_pos, len(block_set), palette, block_list_final)

if __name__ == '__main__':
    ...