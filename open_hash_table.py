hash_table = [0] * 8

def get_key(data):
    return hash(data)

def get_address(key):
    return key % 8

def save_data(data, value):
    key = get_key(data)
    addr = get_address(key)
    if not hash_table[addr]:
        hash_table[addr] = [[key, value]]
    else:
        for i in range(len(hash_table[addr])):
            if hash_table[addr][i][0] == key:
                hash_table[addr][i][1] = value
                return
        hash_table[addr].append([key, value])
                       
def read_data(data):
    key = get_key(data)
    addr = get_address(key)
    if not hash_table[addr]:
       return None
    else:
       for i in range(len(hash_table[addr])):
           if hash_table[addr][i][0] == key:
               return hash_table[addr][i][1]
           return None
