import struct
import gzip


def read_bytes(f, num):
    bytes_read = f.read(num)
    if len(bytes_read) != num:
        raise EOFError("Unexpected end of file.")
    return bytes_read

def TAG_End():
    return None

def TAG_Byte(f):
    return struct.unpack('b', read_bytes(f, 1))[0]

def TAG_Short(f):
    return struct.unpack('>h', read_bytes(f, 2))[0]

def TAG_Int(f):
    return struct.unpack('>i', read_bytes(f, 4))[0]

def TAG_Long (f):
    return struct.unpack('>q', read_bytes(f, 8))[0]

def TAG_Float(f):
    return struct.unpack('>f', read_bytes(f, 4))[0]

def TAG_Double(f):
    return struct.unpack('>d', read_bytes(f, 8))[0]

def TAG_Byte_Array(f):
    array_len = struct.unpack('>i', read_bytes(f, 4))[0]
    byte_list = [0]*array_len

    for i in range(array_len):
        byte_list[i] = struct.unpack('b', read_bytes(f, 1))[0]

    return byte_list

def TAG_String(f):
    string_len = struct.unpack('>H', read_bytes(f, 2))[0]
    return read_bytes(f, string_len).decode('utf-8')

def TAG_List(f):
    global depth
    
    TAG_id = struct.unpack('b', read_bytes(f, 1))[0]
    array_len = struct.unpack('>i', read_bytes(f, 4))[0]
    TAG_type_list = [0]*array_len

    depth += 1

    for i in TAG_type_list:
        TAG_type_list[i] =  read_TAG(f, TAG_id)

    depth -= 1

    return 'Empty' if array_len == 0 else ''
        
def TAG_Compound(f):
    value = ''
    while True:
        if value == None:
            break
        value = read_TAG(f)

def TAG_Int_Array(f):
    array_len = struct.unpack('>i', read_bytes(f, 4))[0]
    int_list = [0]*array_len

    for i in range(array_len):
        int_list[i] = struct.unpack('>i', read_bytes(f, 4))[0]

    return int_list

def TAG_Long_Array(f):
    array_len = struct.unpack('>i', read_bytes(f, 4))[0]
    long_list = [0]*array_len

    for i in range(array_len):
        long_list[i] = struct.unpack('>q', read_bytes(f, 8))[0]

    return long_list


def read_TAG(f, TAG_List_id = None):
    global depth

    if TAG_List_id == None:
        TAG_id = TAG_Byte(f)
    else:
        TAG_id = TAG_List_id

    if TAG_id == 0:
        #display_structure('End TAG', '', depth)
        depth -= 1
        return TAG_End()

    if TAG_List_id == None:
        name = TAG_String(f)

    if TAG_id == 10:
        display_structure(str(TAG_id) + ' ' + name, '', depth)
        depth += 1

        TAG_Compound(f)
        return ''

    if TAG_id == 1:
        value = TAG_Byte(f)
    elif TAG_id == 2:
        value = TAG_Short(f)
    elif TAG_id == 3:
        value = TAG_Int(f)
    elif TAG_id == 4:
        value = TAG_Long(f)
    elif TAG_id == 5:
        value = TAG_Float(f)
    elif TAG_id == 6:
        value = TAG_Double(f)
    elif TAG_id == 7:
        value = TAG_Byte_Array(f)
    elif TAG_id == 8:
        value = TAG_String(f)
    elif TAG_id == 9:
        value = TAG_List(f)
    elif TAG_id == 11:
        value = TAG_Int_Array(f)
    elif TAG_id == 12:
        value = TAG_Long_Array(f)

    display_structure(str(TAG_id) + ' ' + name, value, depth)

    return value


def display_structure(name, value, depth):
    value = f': {value}' if value != '' else value
    print(f'{'     '*max(depth - 1, 0)}{' └───'*min(max(depth, 0), 1)} {name}{value}')


if __name__ != '__main__':
    def display_structure(name, value, depth):
        pass

filename = 'test.schem'
with gzip.open(filename, 'rb') as f:
    depth = 0
    read_TAG(f)
