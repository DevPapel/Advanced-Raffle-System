# PRNG Algorithm #
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


# Weighted Random Algorithm #
def weighted_randomness(chance: list, item: list, total = 0, n = 0, k = 0):
    if total == 0:
        total = sum(chance)
        random_int = gen_randomint(0, total)
        for i in chance:
            n += 1
            k += i
            if random_int <= k:
                return item[n-1]


# Main Menu Function
def main_menu():
    while True:
        try:
            menu = int(input("\n- Main Menu [Select an Option]-\n\n[1] Add a Raffle Prize\n[2] Edit the Raffle Prizes\n[3] Preview Raffle Prizes\n[4] Start the Raffle\n[5] End the Program\n\nHello "+host+", what option would you like to choose? "))
            while menu < 0 or menu > 5:
                menu = int(input("\n- Main Menu [Invalid Option, Please try again]-\n\n[1] Add a Raffle Prize\n[2] Edit the Raffle Prizes\n[3] Preview Raffle Prizes\n[4] Start the Raffle\n[5] End the Program\n\nHello "+host+", what option would you like to choose? "))
            if menu == 1:
                add_newitem()
            elif menu == 2:
                edit_item()
            elif menu == 3:
                preview_raffleItem()
                print("")
                main_menu()
            elif menu == 4:
                spin_item()
            elif menu == 5:
                print("Thank you for using this program! I hope you enjoy using it!")
                exit()
            break
        except ValueError:
            print("Input should only be an integer from the Options")


# Preview items in the raffle
def preview_raffleItem():
    print("\nPreviewing Raffle items to win")
    for i in range(len(item)):
        print("-", item[i], str(chance[i])+"%")

# Add new item in the raffle items
def add_newitem():
    add_item = input("What item do you want to add? ")
    item.append(add_item)

    while True:
        try:
            add_chance = float(input("What is the percentage chance to gett "+str(add_item)+"? "))
            while add_chance <= 0 or add_chance > 100:
                add_chance = float(input("Percentage should be ranging from 1 - 100, type your answer again: "))
            break
        except ValueError:
            print("Answer should be a number (Example Answer: 20) and it automatically converts as 20%")
    chance.append(add_chance)
    print("Raffle Item have successfully been updated")
    preview_raffleItem()

    continue_add = input("\nDo you want to continue adding item? [Y/N]: ").upper()
    if continue_add != "Y":
        print("")
        main_menu()
    else:
        add_newitem()
    
# Edit item in the raffle items
def edit_item():
    while True:
        try:
            print("\n- Editing [Choose an Option] -")
            print("[0] Go back to Main Menu")
            for i in range(len(item)):
                print("["+str(i+1)+"]", item[i], str(chance[i])+"%")
            edit_menu1 = int(input("What item do you want to edit? "))
            while edit_menu1 < 0 or edit_menu1 > len(item):
                print("\n- Editing [Option out of range, please try again] -")
                print("[0] Go back to Main Menu")
                for i in range(len(item)):
                    print("["+str(i+1)+"]", item[i], str(chance[i])+"%")
                edit_menu1 = int(input("What item do you want to edit? "))
            if edit_menu1 != 0:
                edit_menu1 = edit_menu1 - 1
            else:
                print("")
                main_menu()
            break
        except ValueError:
            print("Input should only be an integer from the Options")

    while True:
        try:
            print("\n- Editing "+str(item[edit_menu1]),str(chance[edit_menu1])+"% [Choose an option] -")
            print("[0] Go Back to Main Menu\n[1] Change Item & Chance\n[2] Change the Item\n[3] Change the Chance\n[4] Remove the item from the raffle")
            edit_menu2 = int(input("What do you want to edit from "+str(item[edit_menu1])+" "+str(chance[edit_menu1])+"%? "))
            while edit_menu2 < 0 or edit_menu2 > 4:
                print("\n- Editing "+str(item[edit_menu1]),str(chance[edit_menu1])+"% [Option out of range, Please Try Again] -")
                print("[0] Go Back to Main Menu\n[1] Change Item & Chance\n[2] Change the Item\n[3] Change the Chance\n[4] Remove the item from the raffle")
                edit_menu2 = int(input("What do you want to edit from "+str(item[edit_menu1])+" "+str(chance[edit_menu1])+"%? "))
            if edit_menu2 == 0:
                print("")
                main_menu()
            elif edit_menu2 == 1:
                new_item = input("Type the new item you want to replace "+str(item[edit_menu1]+": "))
                item[edit_menu1] = new_item
                new_chance = float(input("Type the new chance for the item "+str(item[edit_menu1])+": "))
                chance[edit_menu1] = new_chance
                print("Raffle Item have successfully been updated")
                preview_raffleItem()

            elif edit_menu2 == 2:
                new_item = input("Type the new item you want to replace "+str(item[edit_menu1]+": "))
                item[edit_menu1] = new_item
                print("Raffle Item have successfully been updated")
                preview_raffleItem()

            elif edit_menu2 == 3:
                new_chance = float(input("Type the new chance for the item "+str(item[edit_menu1])+": "))
                chance[edit_menu1] = new_chance
                print("Raffle Item have successfully been updated")
                preview_raffleItem()

            elif edit_menu2 == 4:
                del item[edit_menu1]
                del chance[edit_menu1]
                print("Raffle Item have successfully been updated")
                preview_raffleItem()
            break
        except ValueError:
            print("Input should only be an integer from the Options")

    continue_edit = input("\nDo you want to continue editing item? [Y/N]: ").upper()
    if continue_edit != "Y":
        print("")
        main_menu()
    else:
        edit_item()

# Spin the raffle
def spin_item():
    preview_raffleItem()
    while True:
        try:
            spin = int(input("\n- Choose an option -\n[0] Go Back to Main Menu \n[1] Spin 1x\n[2] Spin X Times\nType the option you want: "))
            while spin < 0 or spin > 2:
                spin = int(input("\n- Option out of range, try again -\n[0] Go Back to Main Menu \n[1] Spin 1x\n[2] Spin X Times\nType the option you want: "))
            if spin == 0:
                print("")
                main_menu()
            elif spin == 1:
                winning_prize = weighted_randomness(chance, item)
                print("Congratulations, you got the raffle item: "+winning_prize+"!")
            elif spin == 2:
                spin_option = int(input("How many spin you want to do?[Example answer: 10 - will be 10x Spin]: "))
                for i in range(0, spin_option):
                    print("Congraulations, you got the raffle item: "+weighted_randomness(chance,item)+"!")
            break
        except ValueError:
            print("Input should only be an integer from the Options")
    continue_spin = input("\nDo you want to continue spinning raffle? [Y/N]: ").upper()
    if continue_spin != "Y":
        print("")
        main_menu()
    else:
        spin_item()



# List Variables
item = ["sample prize"]
chance = [1]

# Welcome Message
print("Welcome to the Advanced Raffle System")
host = input("Please enter the Host's Name: ")

# Calling the main_menu
main_menu()