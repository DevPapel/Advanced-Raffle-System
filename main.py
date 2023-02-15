def get_randombits(k: int):
    numbytes = (k + 7) // 8 # bits / 8 and rounded up
    x = int.from_bytes(__import__("os").urandom(numbytes), "big")
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

#item = ["ballpen", "pencil", "paper"]
#chance = [10, 30, 60]     
#x = weighted_randomness(chance, item)
#print(x)

item = ["stone", "sword"]
chance = [1, 2]

print("Welcome to the Advanced Raffle System")
host = input("Please enter the Host's Name: ")

print("Hello",host+", what do you want to do?")
menu = int(input("[1] Add a Raffle Prize\n[2] Edit the Raffle Prizes\n[3] Start the Raffle\n[4] End the Raffle\nEnter your answer: "))

if menu == 1:
    add_item = input("What item do you want to add? ")
    item.append(add_item)

    add_chance = float(input("What is the percentage chance to get "+str(add_item)+"? "))
    chance.append(add_chance)

    print(item)
    print(chance)


elif menu == 2:
    print("\n- Editing [Type the number you want to edit] -")
    for i in range(len(item)):
        print("["+str(i+1)+"]", item[i], str(chance[i])+"%")
    edit_menu1 = int(input("What item do you want to edit? "))
    edit_menu1 = edit_menu1 - 1
    print("\n- Editing "+str(item[edit_menu1]),str(chance[edit_menu1])+"% [Choose an option] -")
    print("[1] Change Item & Chance\n[2] Change the Item\n[3] Change the Chance")

    edit_menu2 = int(input("What do you want to edit from "+str(item[edit_menu1])+" "+str(chance[edit_menu1])+"%? "))
    if edit_menu2 == 1:
        new_item = input("Type the new item you want to replace "+str(item[edit_menu1]+": "))
        item[edit_menu1] = new_item
        new_chance = float(input("Type the new chance for the item "+str(item[edit_menu1])+": "))
        chance[edit_menu1] = new_chance
        print("Raffle Item have successfully been updated")
        for i in range(len(item)):
            print("["+str(i+1)+"]", item[i], str(chance[i])+"%")

    elif edit_menu2 == 2:
        new_item = input("Type the new item you want to replace "+str(item[edit_menu1]+": "))
        item[edit_menu1] = new_item
        print("Raffle Item have successfully been updated")
        for i in range(len(item)):
            print("["+str(i+1)+"]", item[i], str(chance[i])+"%")

    elif edit_menu2 == 3:
        new_chance = float(input("Type the new chance for the item "+str(item[edit_menu1])+": "))
        chance[edit_menu1] = new_chance
        print("Raffle Item have successfully been updated")
        for i in range(len(item)):
            print("["+str(i+1)+"]", item[i], str(chance[i])+"%")







