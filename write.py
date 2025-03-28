import struct
import gzip


def TAG_End(f):
    return None

def TAG_Byte(f):
    struct.pack('b', f.write(f, 1))[0]

def TAG_Short(f):
    struct.pack('>h', write_bytes(f, 2))[0]

def TAG_Int(f):
    struct.pack('>i', write_bytes(f, 4))[0]

def TAG_Long (f):
    struct.pack('>q', write_bytes(f, 8))[0]

def TAG_Float(f):
    struct.pack('>f', write_bytes(f, 4))[0]

def TAG_Double(f):
    struct.pack('>d', write_bytes(f, 8))[0]

def TAG_Byte_Array(f):
    array_len = struct.pack('>i', write_bytes(f, 4))[0]
    byte_list = [0]*array_len

    for i in range(array_len):
        byte_list[i] = struct.pack('b', write_bytes(f, 1))[0]

def TAG_String(f):
    string_len = struct.pack('>H', write_bytes(f, 2))[0]
    write_bytes(f, string_len).decode('utf-8')

def TAG_List(f):
    TAG_id = struct.pack('b', write_bytes(f, 1))[0]
    TAG_id, struct.pack('>i', write_bytes(f, 4))[0]

def TAG_Compound(f):
    value = False
    while True:
        if value == None:
            break


def TAG_Int_Array(f):
    array_len = struct.pack('>i', write_bytes(f, 4))[0]
    int_list = [0]*array_len

    for i in range(array_len):
        int_list[i] = struct.pack('>i', write_bytes(f, 4))[0]

def TAG_Long_Array(f):
    array_len = struct.pack('>i', write_bytes(f, 4))[0]
    long_list = [0]*array_len

    for i in range(array_len):
        long_list[i] = struct.pack('>q', write_bytes(f, 8))[0]


filename = 'new2.schem'
with gzip.open(filename, 'wb') as f:
    ...
