import random as rd
import time
import os
Dividingline = '\t\033[1;91m=============================================\033[0m'
Errorsign = '\t\033[1;91m TYPE ERROR!! PLEASE ENTER THE CORRECT TYPE~\033[0m'
Correct = '\t\033[1;32;1m Correct!!\033[0m'
Sorry = '\t\033[1;90m Guessed wrong!! Please try again~\033[0m'
tryagain = '\t\033[1;90m Please try again~\033[0m'
encourage1 = '\t\033[1;97;1m Dear~Don\'t worry, just try again\033[0m'
encourage2 = '\t\033[1;34;1m Failure is the mother of success\033[0m'
encourage3 = '\t\033[1;33;1m Everyone has something they are good at\033[0m'
encourage4 = '\t\033[1;35;1m I think my patience is running out\033[0m'
encourage5 = '\t\033[1;31;1m Zombies don\'t even want to eat you, they eat brains after all\033[0m'
encourage6 = '\t\033[1;31;1m Have you ever seen a monkey? No? Looks like you never look in the mirror\033[0m'
encourage7 = '\t\033[1;31;1m Although I\'m just a bunch of code, but I want to be a good human being, before I see you\033[0m'
encourage8 = '\t\033[1;31;1m I guess you must be a woman, I\'m sorry I\'m so ungentlemanly\033[0m'
encourage9 = '\t\033[1;31;1m Ape together...strong!\033[0m'
encourage10 = '\t\033[1;31;1m You are the person or animal I have ever seen interact with me for so long and the last one that interacted with me for so long was my creator, that idiot\033[0m'
encourage11 = '\t\033[1;31;1m e04\033[0m'


def arrayget():
    while (1):
        array = [((rd.randint(1, 9)*int(time.time())) % 10)]
        if (array[0] != 0):
            break
    i = 0
    count = 0
    while (i <= 2):
        num = ((rd.randint(0, 9)*int(time.time())) % 10)
        for K in range(0, len(array)):
            if (num != array[K]):
                count += 1
        if (count == len(array)):
            array.append(num)
            i += 1
        count = 0
    return array


def arraycheck(array):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if (array[i] == array[j]):
                return 1
    return 0


def gamestart():
    print('\t\033[1;91m==============================\033[0m')
    print('\t\033[1;31;1m             2A2B\033[0m')
    print('\t\033[1;91m==============================\033[0m')
    print(
        '\t\033[1;32;1m The first word is not zero, the number is not repeated\033[0m')
    print('\t\033[1;32m Enter four numbers~~\033[0m', end=' ')


def arrayinput():
    array = []
    num = 0
    while (1):
        try:
            num = input()
            if(num=="exit"):
                os._exit(1)
            num=int(num)
        except:
            print('\n', Dividingline, '\n', Errorsign, '\n', Dividingline,)
            print(tryagain, end=" ")
            continue
        if (num > 1000 and num < 10000):
            break
        print('\n', Dividingline, '\n', Errorsign, '\n', Dividingline,)
        print(tryagain, end=" ")
    for i in range(0, 4):
        array.append(int(num / (10 ** (3-i))))
        num %= (10 ** (3-i))
    return array


def Anscheak(array, ans):
    cmparray = []
    for i in array:
        cmparray.append(i)
    Anslist = []
    Anum = 0
    Bnum = 0
    for i in range(0, 4):
        if (array[i] == ans[i]):
            cmparray.remove(array[i])
            Anum += 1
    Anslist.append(Anum)
    for i in range(0, len(cmparray)):
        for j in range(0, len(ans)):
            if (cmparray[i] == ans[j]):
                Bnum += 1
    Anslist.append(Bnum)
    print('\t\033[1;37;1m',Anslist[0], 'A', Anslist[1], 'B')
    if (Anslist[0] == 4):
        return 1
    return 0
