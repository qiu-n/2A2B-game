import gamefunction as gf
Game_Nunbers = 0
if __name__ == "__main__":
    #get password 
    passwd = gf.random_algorithm()
    #print gamestart
    gf.print_gamestart()
    #game-while
    while 1:
        ans = gf.input_ans()
        Game_Nunbers += 1
        if gf.Anscheak(passwd, ans) == True:
            break
        gf.print_encourag(Game_Nunbers)
    #game end    
    print(gf.Correct)
