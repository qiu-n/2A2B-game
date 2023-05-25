import random as rd
import os
from typing import List

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
    "\t\033[1;31;1m I guess you must be a woman, I'm sorry I'm so ungentlemanly \033[0m"
)
encourage9 = "\t\033[1;31;1m Ape together...strong!\033[0m"
encourage10 = "\t\033[1;31;1m You are the person or animal I have ever seen interact with me for so long and the last one that interacted with me for so long was my creator, that idiot\033[0m"
encourage11 = "\t\033[1;31;1m e04\033[0m"


def random_algorithm() -> List[int]:
    # get first passwd
    passwd = [rd.randint(1, 9)]

    # get other passwd
    sequence = [i for i in range(0, 10)]
    # remove first passwd
    sequence.remove(passwd[0])
    passwd += rd.sample(sequence, 3)
    return passwd


def input_ans() -> List[int]:
    while 1:
        # get answer in list
        ans: List[str] = list(input())

        # check exit
        if ans == ["e", "x", "i", "t"]:
            os._exit(1)

        # check answer type
        if check_array(ans) == True:
            break
        print_error()

    # answer turn into list(int)
    ans_new = [int(x) for x in ans]
    return ans_new


def check_array(array: List[str]) -> bool:
    # check repetition and length
    if len(set(array)) != 4 or len(array) != 4:
        return False
    # check first answer
    if array[0] == "0":
        return False
    # checklist not in English
    for i in array:
        if str(i).isdigit() != True:
            return False
    return True


def Anscheak(array: List[int], ans: List[int]) -> bool:
    # check ans==passwd
    if array == ans:
        print("\t\033[1;37;1m", "4", "A", "0", "B")
        return True
    # get a few 'A' a few 'B' and return by list
    Anslist: List[int] = [0, 0]
    for i in range(0, 4):
        for j in range(0, 4):
            if array[i] == ans[j]:
                if i == j:
                    Anslist[0] += 1
                else:
                    Anslist[1] += 1
    print("\t\033[1;37;1m", Anslist[0], "A", Anslist[1], "B")
    return False


def print_error():
    print(
        "\n",
        Dividingline,
        "\n",
        Errorsign,
        "\n",
        Dividingline,
    )
    print(tryagain, end=" ")


def print_encourage(count: int):
    if count == 3:
        print(encourage1)
    elif count == 6:
        print(encourage2)
    elif count == 9:
        print(encourage3)
    elif count == 12:
        print(encourage4)
    elif count == 15:
        print(encourage5)
    elif count == 18:
        print(encourage6)
    elif count == 21:
        print(encourage7)
    elif count == 24:
        print(encourage8)
    elif count == 27:
        print(encourage9)
    elif count == 30:
        print(encourage10)
    elif count > 30:
        print(encourage11)
    print(Sorry, end=" ")


def print_gamestart():
    print("\t\033[1;91m==============================\033[0m")
    print("\t\033[1;31;1m             2A2B\033[0m")
    print("\t\033[1;91m==============================\033[0m")
    print(
        "\t\033[1;32;1m The first word is not zero, the number is not repeated\033[0m"
    )
    print("\t\033[1;32m Enter four numbers~~\033[0m", end=" ")
