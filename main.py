from gamefunction import (
    random_algorithm,
    print_gamestart,
    Anscheak,
    input_ans,
    print_encourag,
    Correct
)

Game_Nunbers = 0
if __name__ == "__main__":
    # get password
    passwd = random_algorithm()
    # print gamestart
    print_gamestart()
    # game-while
    while 1:
        ans = input_ans()
        Game_Nunbers += 1
        if Anscheak(passwd, ans) == True:
            break
        print_encourag(Game_Nunbers)
    # game end
    print(Correct)
