import random as rd
import os

Dividingline = "\t\033[1;91m=============================================\033[0m"
Errorsign = "\t\033[1;91m TYPE ERROR!! PLEASE ENTER THE CORRECT TYPE~\033[0m"
Correct = "\t\033[1;32;1m Correct!!\033[0m"
Sorry = "\t\033[1;90m Guessed wrong!! Please try again~\033[0m"
tryagain = "\t\033[1;90m Please try again~\033[0m"
encourage1 = "\t\033[1;97;1m Dear~Don't worry, just try again\033[0m"
encourage2 = "\t\033[1;34;1m Failure is the mother of success\033[0m"
encourage3 = "\t\033[1;33;1m Everyone has something they are good at\033[0m"
encourage4 = "\t\033[1;35;1m I think my patience is running out\033[0m"
encourage5 = "\t\033[1;31;1m Zombies don't even want to eat you, they eat brains after all\033[0m"
encourage6 = "\t\033[1;31;1m Have you ever seen a monkey? No? Looks like you never look in the mirror\033[0m"
encourage7 = "\t\033[1;31;1m Although I'm just a bunch of code, but I want to be a good human being, before I see you\033[0m"
encourage8 = (
    "\t\033[1;31;1m I guess you must be a woman, I'm sorry I'm so ungentlemanly\033[0m"
)
encourage9 = "\t\033[1;31;1m Ape together...strong!\033[0m"
encourage10 = "\t\033[1;31;1m You are the person or animal I have ever seen interact with me for so long and the last one that interacted with me for so long was my creator, that idiot\033[0m"
encourage11 = "\t\033[1;31;1m e04\033[0m"


def passwdget():
    array = [rd.randint(1, 9)]
    num = [i for i in range(0, 10)]
    num.remove(array[0])
    rd.shuffle(num)
    array.extend(num[:3])
    return array


def arraycheck(array):
    if len(set(array)) != 4 or len(array) != 4:
        return True
    if array[0] == 0:
        return True
    try:
        array2 = [int(i) for i in array]
        return False
    except:
        return True
    

def gamestart():
    print("\t\033[1;91m==============================\033[0m")
    print("\t\033[1;31;1m             2A2B\033[0m")
    print("\t\033[1;91m==============================\033[0m")
    print(
        "\t\033[1;32;1m The first word is not zero, the number is not repeated\033[0m"
    )
    print("\t\033[1;32m Enter four numbers~~\033[0m", end=" ")


def printerror():
    print(
        "\n",
        Dividingline,
        "\n",
        Errorsign,
        "\n",
        Dividingline,
    )
    print(tryagain, end=" ")


def ansinput():
    while 1:
        ans = list(input())
        if ans == ["e", "x", "i", "t"]:
            os._exit(1)
        if arraycheck(ans) == True:
            printerror()
            continue
        if arraycheck(ans) == False:
            break
    ans_new=[int(x) for x in ans]
    return ans_new


def Anscheak(array, ans):
    Anslist = [0, 0]
    for i in range(0, 4):
        for j in range(0, 4):
            if array[i] == ans[j]:
                if i == j:
                    Anslist[0] += 1
                else:
                    Anslist[1] += 1
    print("\t\033[1;37;1m", Anslist[0], "A", Anslist[1], "B")
    if Anslist[0] == 4:
        return True
    return False
