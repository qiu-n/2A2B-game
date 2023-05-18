import gamefunction as gf

if __name__ == "__main__":
    array = gf.passwdget()
    gf.gamestart()
    count = 0
    while 1:
        ans = gf.ansinput()
        count += 1
        if gf.Anscheak(array, ans) == True:
            break
        elif count == 3:
            print(gf.encourage1)
        elif count == 6:
            print(gf.encourage2)
        elif count == 9:
            print(gf.encourage3)
        elif count == 12:
            print(gf.encourage4)
        elif count == 15:
            print(gf.encourage5)
        elif count == 18:
            print(gf.encourage6)
        elif count == 21:
            print(gf.encourage7)
        elif count == 24:
            print(gf.encourage8)
        elif count == 27:
            print(gf.encourage9)
        elif count == 30:
            print(gf.encourage10)
        elif count > 30:
            print(gf.encourage11)
        print(gf.Sorry, end=" ")
    print(gf.Correct)
