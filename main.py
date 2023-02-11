from os import urandom

def get_randombits(k: int):
    numbytes = (k + 7) // 8 # bits / 8 and rounded up
    x = int.from_bytes(urandom(numbytes), "big")
    return x >> (numbytes * 8 - k) # trimming excess bits
    
print(get_randombits(100))