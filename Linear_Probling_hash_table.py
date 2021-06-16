hash_table = [0] * 8

def get_key(data):
    return hash(data)

def get_addr(key):
    return key % 8

def get_new_addr(addr):
    return (addr+1) % 8

def save_data(data, value):
    key = get_key(data)
    addr = get_addr(key)
    while hash_table[addr]:
        if hash_table[addr][0] == key:
            hash_table[addr][1] = value
            return
        else:
            addr = get_new_addr(addr)
    hash_table[addr] = [key, value]
    
def read_data(data):
    key = get_key(data)
    addr = get_addr(key)
    while hash_table[addr]:
        if hash_table[addr][0] == key:
            return hash_table[addr][1]
        else:
            addr = get_new_addr(addr)
    return None
