from os import urandom

def get_randombits(k: int):
    numbytes = (k + 7) // 8 # bits / 8 and rounded up
    x = int.from_bytes(urandom(numbytes), "big")
    print(x)
    
get_randombits(100)