import time

def tekengalg():

    if stage == 0:
        print("")

    elif stage == 1:
        print("-----------")

    elif stage == 2:
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-----------")

    elif stage == 3:
        print("| /")
        print("|/")
        print("|")
        print("|")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 4:
        print("-----------")
        print("| /")
        print("|/")
        print("|")
        print("|")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 5:
        print("-----------")
        print("| /       |")
        print("|/")
        print("|")
        print("|")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 6:
        print("-----------")
        print("| /       |")
        print("|/        0")
        print("|")
        print("|")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 7:
        print("-----------")
        print("| /       |")
        print("|/        0")
        print("|         |")
        print("|         |")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 8:
        print("-----------")
        print("| /       |")
        print("|/        0")
        print("|        \\|/")
        print("|         |")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 9:
        print("-----------")
        print("| /       |")
        print("|/        0")
        print("|        \\|/")
        print("|         |")
        print("|\\")
        print("| \\")
        print("-----------")

    elif stage == 10:
        print("-----------")
        print("| /       |")
        print("|/        0")
        print("|        \\|/")
        print("|         |")
        print("|\\       / \\")
        print("| \\")
        print("-----------")

stage = 0
gebruikt = ""
woord = input("een galgje woord: ")
if not woord.isdigit():
    leng = len(woord)
    print("\n"*100)
    streep = "-"*leng
    while True:
        print("\n"*100)
        print(streep)
        print("")
        print("deze letters heb je gebruikt: " + gebruikt)
        print("")
        tekengalg()
        letter = input("welke letter zit er in het woord: ")
        lengletter = len(letter)
        if not letter.isdigit():
            if lengletter < 2:
                if letter in gebruikt:
                    print("deze letter heb je al gebruikt")
                    time.sleep(1.5)
                elif letter == "?":
                    raad = input("welk woor denk je dat het is: ")
                    if raad == woord:
                        print("Jeeeee je hebt het geraden :)")
                        break
                    else:
                        print("nee dat is niet het woord")
                        stage += 1
                        time.sleep(1.5)
                elif letter in woord:
                    print("ja de letter " + letter + " zit in het woord")
                    for i in range(leng):
                        if woord[i] == letter:
                            streep = streep[:i] + letter + streep[i+1:]
                    gebruikt = gebruikt + "," + letter
                else:
                    print("nee de letter " + letter + " zit niet in het woord")
                    stage += 1
                    gebruikt = gebruikt + "," + letter
                if stage == 10:
                    print("")
                    tekengalg()
                    print("jammer je bent gestikt")
                    print("het woord was " + woord)
                    break
                if streep == woord:
                    print("Jeeeee je hebt het geraden :)")
                    break
            else:
                print("dit is een woord geen letter")
                time.sleep(1.5)
        else:
            print("je gebruikt cijfers")
            time.sleep(1.5)
else:
    print("je woord bestaat uit cijfers, probeer overnieuw")
print("")
print("tot volgende keer")

