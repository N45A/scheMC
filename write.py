import struct
import gzip


def TAG_End():
    pass

def TAG_Byte(f, data):
    f.write(struct.pack('b', data))

def TAG_Short(f, data):
    f.write(struct.pack('>h', data))

def TAG_Int(f, data):
    f.write(struct.pack('>i', data))

def TAG_Long (f, data):
    f.write(struct.pack('>q', data))

def TAG_Float(f, data):
    f.write(struct.pack('>f', data))

def TAG_Double(f, data):
    f.write(struct.pack('>d', data))

def TAG_Byte_Array(f, data):
    f.write(struct.pack('>i', len(data)))

    for b in data:
        f.write(struct.pack('b', b))

def TAG_String(f, data):
    data = data.encode('utf-8')

    f.write(struct.pack('>H', len(data)))
    f.write(data)

def TAG_List(f, data):
    TAG_id = data[0]
    f.write(struct.pack('b', TAG_id))

    array_len = len(data[1:])
    f.write(struct.pack('>i', array_len))

    for d in data[1:]:
        write_TAG(f, TAG_id, d=d, write_TAG_id=False)

def TAG_Compound(f, data):
    name = data[0]
    TAG_String(f, name)

    for d in data[1:]:
        TAG_id, name, value = d
        write_TAG(f, TAG_id, name=name, d=value)

def TAG_Int_Array(f, data):
    f.write(struct.pack('>i', len(data)))

    for b in data:
        f.write(struct.pack('>i', b))

def TAG_Long_Array(f, data):
    f.write(struct.pack('>i', len(data)))

    for b in data:
        f.write(struct.pack('>q', b))


def write_TAG(f, TAG_id, name=None, d=None, write_TAG_id=True):
    if write_TAG_id:
        TAG_Byte(f, TAG_id)

    if name != None:
        TAG_String(f, name)

    if TAG_id == 0:
        TAG_End()
    if TAG_id == 1:
        TAG_Byte(f, d)
    elif TAG_id == 2:
        TAG_Short(f, d)
    elif TAG_id == 3:
        TAG_Int(f, d)
    elif TAG_id == 4:
        TAG_Long(f, d)
    elif TAG_id == 5:
        TAG_Float(f, d)
    elif TAG_id == 6:
        TAG_Double(f, d)
    elif TAG_id == 7:
        TAG_Byte_Array(f, d)
    elif TAG_id == 8:
        TAG_String(f, d)
    elif TAG_id == 9:
        TAG_List(f, d)
    elif TAG_id == 10:
        TAG_Compound(f, d)
    elif TAG_id == 11:
        TAG_Int_Array(f, d)
    elif TAG_id == 12:
        TAG_Long_Array(f, d)

filename = 'test.schem'
with gzip.open(filename, 'wb') as f:
    write_TAG(f, 10, d=[
        'Schematic',
        [3, 'Version', 1],
        [3, 'DataVersion', 3837],
        [10, None, [
            'Metadata',
            [3, 'WEOffsetX', 0],
            [3, 'WEOffsetY', 0],
            [3, 'WEOffsetZ', 0],
            [10, None, [
                'MCSchematicMetadata',
                [8, 'Generated', 'Generated with Nasa\'s scheMC'],
                [0, None, None]
            ]],
            [0, None, None]
        ]],
        [2, 'Height', 2],
        [2, 'Length', 2],
        [2, 'Width', 2],
        [3, 'PaletteMax', 3],
        [10, None, [
            'Palette',
            [3, 'minecraft:air', 0],
            [3, 'minecraft:lime_stained_glass', 1],
            [3, 'minecraft:diamond_block', 2],
            [0, None, None]
        ]],
        [7, 'BlockData', [1, 0, 0, 0, 0, 0, 0, 2]],
        [9, 'BlockEntities', [0]],
        [0, None, None]
    ])