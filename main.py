from os import urandom

def get_randombits(k: int):
    numbytes = (k + 7) // 8 # bits / 8 and rounded up
    x = int.from_bytes(urandom(numbytes), "big")
    return x >> (numbytes * 8 - k) # trimming excess bits

def gen_randomint(min: int, max: int):
    max += 1

    width = max - min
    random_pref = 0

    if width > 0:
        k = width.bit_length()
        random_pref = get_randombits(k)

        while random_pref >= width:
            random_pref = get_randombits(k)
    return min+random_pref


def weighted_randomness(chance: list, item: list, total = 0, n = 0, k = 0):
    if total == 0:
        total = sum(chance)
        random_int = gen_randomint(0, total)
        for i in chance:
            n += 1
            k += i
            if random_int <= k:
                return item[n-1]

item = ["ballpen", "pencil", "paper"]
chance = [10, 30, 60]     
x = weighted_randomness(chance, item)
print(x)