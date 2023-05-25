from gamefunction import (
    random_algorithm,
    print_gamestart,
    Anscheak,
    input_ans,
    print_encourage,
    Correct,
    List,
)

Game_Nunbers = 0
if __name__ == "__main__":
    # get password
    passwd = random_algorithm()
    # print gamestart
    print_gamestart()
    # game-while
    while 1:
        ans: List[int] = input_ans()
        Game_Nunbers += 1
        if Anscheak(passwd, ans) == True:
            break
        print_encourage(Game_Nunbers)
    # game end
    print(Correct)
