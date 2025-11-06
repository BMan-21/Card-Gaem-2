from time import sleep
from random import randint
#(i) prefix 3 for text, 4 for bg, 9 for bright text, 10 for bright bg
#(i) \x1b[38;2;r;g;bm for rgb Text, \x1b[48;2;r;g;bm for rgb Background
#(i) \x1b[38;5;___m for 256 Text\x1b[48;5;___m for 256 Background, https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/extended-256-colors/#structure for all 256
#(v) the following are text
red = "\x1b[31m"
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
yellowbg = "\x1b[43m"
greenbg = "\x1b[42m"
bluebg = "\x1b[44m"
cyanbg = "\x1b[46m"
magentabg = "\x1b[45m"
whitebg = "\x1b[107m"
blackbg = "\x1b[40m"
reset = "\x1b[0m"
print(red + "Welcome" + magenta + " to" + yellow + " card" + green + " gaem" + blue + " 2" + reset)
print("nothing yet!")
money = 16
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
            pack = input("what pack do you want to open? 1. base pack ("+yellow+"16"+reset+" money), 2. booster pack ("+yellow+"20"+reset+" money), 3. mega pack (" + yellow + "50" + reset + " money) you have " + yellow + str(money) + reset + " money: ")
            if pack == "1":
                #base pack
                if money >= 16:
                    money -= 16
                #(v) pack stuff
                    print("opening pack...")
                    #(v) find cards
                    card1 = randint(1,100)
                    card2 = randint(1,100)
                    card3 = randint(1,100)
                    cards = [card1, card2, card3]
                    cards.sort()
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
                    packanim(reset)
                    sleep(0.5)
                    print(colors[0] + " ______________" )
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
                    sleep(1)
                    print(colors[1] + " ______________")
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
                    sleep(1)
                    print(colors[2] + " ______________")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
            elif pack == "2":
                if money >= 20:
                    money -= 20
                    print("opening pack...")
                    #(v) find cards
                    card1 = randint(1,100)
                    card2 = randint(1,100)
                    cards = [card1, card2]
                    cards.sort()
                    colors = []
                    for c in cards:
                        #(v) common (40%)
                        if c <= 40:
                            binder.append("common")
                            colors.append(blue)
                        #(v) uncommon (30%)
                        elif c > 40 and c <= 70:
                            binder.append("uncommon")
                            colors.append(green)
                        #(v) rare (30%)
                        elif c > 70 and c <= 100:
                            binder.append("rare")
                            colors.append(cyan)
                    #card animation
                    packanim(reset)
                    sleep(0.5)
                    print(colors[0] + " ______________" )
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
                    sleep(1)
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
                        if c <= 40:
                            print(blue + "common" + reset)
                        elif c > 40 and c <= 70:
                            print(green + "uncommon" + reset)
                        elif c > 70 and c <= 100:
                            print(cyan + "rare" + reset)
            #mega pack
            elif pack == "3":
                if money >= 50:
                    money -= 50
                    print("opening pack...")
                    #(v) find cards
                    card1 = randint(1,100)
                    card2 = randint(1,100)
                    card3 = randint(1,100)
                    card4 = randint(1,100)
                    card5 = randint(1,100)
                    card6 = randint(1,100)
                    cards = [card1, card2, card3, card4, card5, card6]
                    cards.sort()
                    colors = []
                    for c in cards:
                        #(v) common (30%)
                        if c <= 30:
                            binder.append("common")
                            colors.append(blue)
                        #(v) uncommon (10%)
                        elif c > 30 and c <= 40:
                            binder.append("uncommon")
                            colors.append(green)
                        #(v) rare (30%)
                        elif c > 40 and c <= 70:
                            binder.append("rare")
                            colors.append(cyan)
                        #(v) epic (20%)
                        elif c > 70 and c <= 90:
                            binder.append("epic")
                            colors.append(magenta)  
                        #(v) legendary (10%)
                        elif c > 90 and c <= 100:
                            binder.append("legendary")
                            colors.append(yellow)
                    #card animation
                    packanim(reset)
                    sleep(0.5)
                    print(colors[0] + " ______________" )
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
                    sleep(1)
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
                    sleep(1)
                    print(colors[2] + " ______________ ")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[3] + " ______________ ")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[4] + " ______________ ")
                    print(colors[4] + "/" + colors[3] + "______________" + colors[4] + "\\")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[5] + " ______________ ")
                    print(colors[5] + "/" + colors[4] + "______________" + colors[5] + "\\")
                    print(colors[4] + "/" + colors[3] + "______________" + colors[4] + "\\")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                        if c <= 30:
                            print(blue + "common" + reset)
                        elif c > 30 and c <= 40:
                            print(green + "uncommon" + reset)
                        elif c > 40 and c <= 70:
                            print(cyan + "rare" + reset)
                        elif c > 70 and c <= 90:
                            print(magenta + "epic" + reset)  
                        elif c > 90 and c <= 100:
                            print(yellow + "legendary" + reset)   
                else:
                    print("u kinda broke")
                
            elif pack == "4":
                if money >= 75:
                    money -= 75
                    print("opening pack...")
                    #(v) find cards
                    card1 = randint(1,100)
                    card2 = randint(1,100)
                    card3 = randint(1,100)
                    card4 = randint(1,100)
                    card5 = randint(1,100)
                    card6 = randint(1,100)
                    cards = [card1, card2, card3, card4, card5, card6]
                    cards.sort()
                    colors = []
                    for c in cards:
                        #(v) common (15%)
                        if c <= 15:
                            binder.append("common")
                            colors.append(blue)
                        #(v) uncommon (10%)
                        elif c > 15 and c <= 25:
                            binder.append("uncommon")
                            colors.append(green)
                        #(v) rare (35%)
                        elif c > 25 and c <= 60:
                            binder.append("rare")
                            colors.append(cyan)
                        #(v) epic (20%)
                        elif c > 60 and c <= 80:
                            binder.append("epic")
                            colors.append(magenta)  
                        #(v) legendary (10%)
                        elif c > 80 and c <= 90:
                            binder.append("legendary")
                            colors.append(yellow)
                        #(v) mythic (10%)
                        elif c > 90 and c <= 100:
                            binder.append("mythic")
                            colors.append(red)
                    #card animation
                    packanim(reset)
                    sleep(0.5)
                    print(colors[0] + " ______________" )
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
                    sleep(1)
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
                    sleep(1)
                    print(colors[2] + " ______________ ")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[3] + " ______________ ")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[4] + " ______________ ")
                    print(colors[4] + "/" + colors[3] + "______________" + colors[4] + "\\")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                    sleep(1)
                    print(colors[5] + " ______________ ")
                    print(colors[5] + "/" + colors[4] + "______________" + colors[5] + "\\")
                    print(colors[4] + "/" + colors[3] + "______________" + colors[4] + "\\")
                    print(colors[3] + "/" + colors[2] + "______________" + colors[3] + "\\")
                    print(colors[2] + "/" + colors[1] + "______________" + colors[2] + "\\")
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
                        if c <= 15:
                            print(blue + "common" + reset)
                        elif c > 15 and c <= 25:
                            print(green + "uncommon" + reset)
                        elif c > 25 and c <= 60:
                            print(cyan + "rare" + reset)
                        elif c > 60 and c <= 80:
                            print(magenta + "epic" + reset)  
                        elif c > 80 and c <= 90:
                            print(yellow + "legendary" + reset)
                        elif c > 90 and c <= 100:
                            print(red + "mythic" + reset)
                else:
                    print("u kinda broke")

            elif pack != 1 and pack != 2 and pack != 3 and pack != 4:
                print("typo, anyone?")
        #sell cards
        if shop == "2":
            common = 0
            uncommon = 0
            rare = 0
            epic = 0
            legendary = 0
            mythic = 0
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
            #add epic + legendary
            sell = input("what card do you want to sell? you have 1. "+ blue + str(common) + " common" + reset + " (" + yellow + "5" + reset + " money), 2. "+ green + str(uncommon) + " uncommon" + reset + " (" + yellow + "7" + reset + " money), 3. " + cyan + str(rare) + " rare" + cyan + " (" + yellow + "12" + reset + " money), 4. " + magenta + str(epic) + " epic" + reset + " (" + yellow + "15" + reset + " money), 5. " + yellow + str(legendary) + " legendary" + reset + " (" + yellow + "25" + reset + " money), 6. "+ red + str(mythic) + " mythic" + reset + " (" + yellow + "30" + reset + "money) or type \"all\" to sell all: ")
            if sell == "1": #(!) finish pls
                num = input("how many commons do you want to sell for 5 money each? you have " + str(common) + ": ")
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
            elif sell == "2":
                num = input("how many uncommons do you want to sell for 7 money each? you have " + str(uncommon) + ": ")
                if int(num) > uncommon:
                    print("u cant count")
                    print("sold all ur uncommons")
                    money += uncommon * 7
                    for i in binder:
                        if i == "uncommon":
                            binder.remove("uncommon")
                if int(num) <= uncommon:
                    print("sold " + str(num) + " uncommons")
                    money += int(num) * 7
                    for i in binder:
                        if i == "uncommon" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("uncommon")
            elif sell == "3":
                num = input("how many rares do you want to sell for 12 money each? you have " + str(rare) + ": ")
                if int(num) > rare:
                    print("u cant count")
                    print("sold all ur rares")
                    money += rare * 12
                    for i in binder:
                        if i == "rare":
                            binder.remove("rare")
                if int(num) <= rare:
                    print("sold " + str(num) + " rares")
                    money += int(num) * 12
                    for i in binder:
                        if i == "rare" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("rare")
            elif sell == "4":
                num = input("how many epics do you want to sell for 15 money each? you have " + str(rare) + ": ")
                if int(num) > rare:
                    print("u cant count")
                    print("sold all ur epics")
                    money += rare * 15
                    for i in binder:
                        if i == "rare":
                            binder.remove("epics")
                if int(num) <= rare:
                    print("sold " + str(num) + " legendarys")
                    money += int(num) * 15
                    for i in binder:
                        if i == "rare" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("rare")
            elif sell == "5":
                num = input("how many legendarys do you want to sell for 20 money each? you have " + str(rare) + ": ")
                if int(num) > legendary:
                    print("u cant count")
                    print("sold all ur legendarys")
                    money += rare * 25
                    for i in binder:
                        if i == "legendary":
                            binder.remove("legendary")
                if int(num) <= legendary:
                    print("sold " + str(num) + " legendarys")
                    money += int(num) * 25
                    for i in binder:
                        if i == "legedary" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("legendary")
            elif sell == "6":
                num = input("how many mythics do you want to sell for 20 money each? you have " + str(rare) + ": ")
                if int(num) > mythic:
                    print("u cant count")
                    print("sold all ur mythics")
                    money += rare * 30
                    for i in binder:
                        if i == "mythic":
                            binder.remove("mythic")
                if int(num) <= mythic:
                    print("sold " + str(num) + " mythic")
                    money += int(num) * 30
                    for i in binder:
                        if i == "mythic" and int(num) > 0:
                            num = int(num) - 1
                            binder.remove("mythic")
            elif sell == "all":
                for c in binder:
                    if c == "common":
                        money += 5
                    if c == "uncommon":
                        money += 7
                    if c == "rare":
                        money += 12
                    if c == "epic":
                        money += 15
                    if c == "legendary":
                        money += 25
                    if c == "mythic":
                        money += 30
                binder = []

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
                print(magenta + c + reset)
            elif c == "legendary":
                print(yellow + c + reset)
            elif c == "mythic":
                print(red + c + reset)
            else:
                print("error")
    elif menu != "1" and menu != "2" and menu != "3":
        print("bro cant type numbers")
#v 0.1.0

