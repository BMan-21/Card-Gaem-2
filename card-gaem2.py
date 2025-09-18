from time import sleep
from random import randint
#(i) prefix 3 for text, 4 for bg, 9 for bright text, 10 for bright bg
#(i) \x1b[38;2;r;g;bm for rgb Text, \x1b[48;2;r;g;bm for rgb Background
#(i) \x1b[38;5;___m for 256 Text\x1b[48;5;___m for 256 Background, https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/extended-256-colors/#structure for all 256
#(v) the following are text
red = "\x1b[31m"
orange = "\x1b[38;5;208m" #(!) not working
yellow = "\x1b[33m"
green = "\x1b[32m"
blue = "\x1b[34m"
cyan = "\x1b[36m"
magenta = "\x1b[35m"
white = "\x1b[97m"
black = "\x1b[30m"
reset = "\x1b[0m"
#(v) the following are bgs
redbg = "\x1b[41m"
orangebg = "\x1b[48;5;208m" #(!) not working
yellowbg = "\x1b[43m"
greenbg = "\x1b[42m"
bluebg = "\x1b[44m"
cyanbg = "\x1b[46m"
magentabg = "\x1b[45m"
whitebg = "\x1b[107m"
blackbg = "\x1b[40m"
reset = "\x1b[0m"
print(red + "Welcome" + orange + " to" + yellow + " card" + green + " gaem" + blue + " 2" + reset)
print("nothing yet!")
money = 100
binder = []
def packanim(color):
    print(color)
    print(" ______________ ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("                ")
    print(" _____________/ ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("              /  ")
    print(" ____________/ ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("              _")
    print("             /   ")
    print(" ___________/ ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|") 
    sleep(0.1)
    print("             __")
    print("            /   ")
    print(" __________/ ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("            ___")
    print("           /")
    print(" _________/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("           ____")
    print("          /")
    print(" ________/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("          _____")
    print("         /")
    print(" _______/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("         ______")
    print("        /")
    print(" ______/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("        _______")
    print("       /")
    print(" _____/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("       ________")
    print("      /")
    print(" ____/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|") 
    sleep(0.2)
    print("      _________")
    print("     /")
    print(" ___/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|") 
    sleep(0.1)
    print("     __________")
    print("    /")
    print(" __/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)
    print("    ___________")
    print("   /")
    print(" _/")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|") 
    sleep(0.1)
    print("   ____________")
    print("  /")
    print(" /")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1)    
    print("  _____________")
    print(" /")
    print(" ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")
    sleep(0.1) 
    print(" ______________")
    print(" ")
    print(" ")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|              |")
    print("|______________|")    
while True:
    print("you have " + yellow + str(money) + reset + " money")
    menu = input("1. shop - 2. binder: ")
    if menu == "1":
        shop = input("1. buy packs - 2. sell cards: ")
        if shop == "1":
            pack = input("what pack do you want to open? 1. base pack (10 money), " + red + "2. booster pack (coming soon!) " + reset + "you have " + yellow + str(money) + reset + " money: ")
            if pack == "1":
                #base pack
                if money >= 10:
                    money -= 10
                #(v) pack stuff
                    print("opening pack...")
                    #(v) find cards
                    card1 = randint(1,100)
                    card2 = randint(1,100)
                    cards = [card1, card2]
                    colors = []
                    for c in cards:
                        #(v) common (75%)
                        if c <= 75:
                            binder.append("common")
                            colors.append(blue)
                        #(v) uncommon (25%)
                        elif c > 75 and c <= 100:
                            binder.append("uncommon")
                            colors.append(green)
                    #card animation
                    #(!) sort cards
                    #(!) reveal 1 at a time
                    print(card1)
                    packanim(reset)
                    sleep(0.1)
                    print(colors[1] + " ______________ ")
                    print(colors[1] + "/" + colors[0] + "______________" + colors[1] + "\\")
                    print(colors[0] + "/" + reset + "______________" + colors[0] + "\\")
                    print(reset + "|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|              |")
                    print("|______________|")
                    sleep(0.5)
                    print("you got:")
                    #(v) replace with something more efficient later
                    for c in cards:
                        if c <= 75:
                            print(blue + "common" + reset)
                        elif c > 75 and c <= 100:
                            print(green + "uncommon" + reset)
                else:
                    print("u really broke")
            #booster pack
            if pack == "2":
                if money >= 15:
                    money -= 15
                    print("imma maek shop first sry")
                else:
                    print("u kinda broke")

            elif pack != "1" and pack != "2":
                print("typo, anyone?")
        #sell cards
        if shop == "2":
            common = 0
            uncommon = 0
            rare = 0
            epic = 0
            legendary = 0
            mythic = 0
            godlike = 0
            for c in binder:
                if c == "common":
                    common += 1
                elif c == "uncommon":
                    uncommon += 1
                elif c == "rare":
                    rare += 1
                elif c == "epic":
                    epic += 1
                elif c == "legendary":
                    legendary += 1
                elif c == "mythic":
                    mythic += 1
                elif c == "godlike":
                    godlike += 1
            sell = input("what card do you want to sell? you have 1. " + str(common) + " common (5 money), 2. " + str(uncommon) + " uncommon (7 money), 3. " + str(rare) + " rare (" + red + "unavailable" + reset + "), 4. " + str(epic) + " epic (" + red + "unavailable" + reset + "), 5. " + str(legendary) + " legendary (" + red + "unavailable" + reset + "), 6. " + str(mythic) + " mythic (" + red + "unavailable" + reset + "), 7. " + str(godlike) + " godlike: " + red + "unavailable" + reset + ": ")
            if sell == "1": #(!) finish pls
                num = input("how many commons do you want to sell for 6 money each? you have " + str(common) + ": ")
                if int(num) > common:
                    print("u cant count")
                    print("sold all ur commons")
                    money += common * 5
                    for i in binder:
                        if i == "common":
                            binder.remove("common")
                if int(num) <= common:
                    print("sold " + str(num) + " commons")
                    money += int(num) * 5
                    for i in binder:
                        if i == "common" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("common")

    elif menu == "2":
        print("you have " + str(len(binder)) + " cards in your binder")
        for c in binder:
            if c =="common":
                print(blue + c + reset)
            elif c == "uncommon":
                print(green + c + reset)
            elif c == "rare":
                print(cyan + c + reset)
            elif c == "epic":
                print(orange + c + reset)
            elif c == "legendary":
                print(yellow + c + reset)
            elif c == "mythic":
                print(red + c + reset)
            elif c == "godlike":
                print(magenta + c + reset)
            else:
                print("error")
    elif menu != "1" and menu != "2" and menu != "3":
        print("bro cant type numbers")
#vNA

