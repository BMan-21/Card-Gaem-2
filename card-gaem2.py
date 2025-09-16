from time import sleep
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
def packanim(color):
    print(color)
    print("  ______________ ")
    print(" /              \\")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print(" |              |")
    print("\\              /")        
while True:
    menu = input("1. shop - 2. binder: ")
    if menu == "1":
        "no shop yet!"
    elif menu == "2":
        print("test animation:")
        sleep(0.5)
        packanim(red)
    else:
        print()

