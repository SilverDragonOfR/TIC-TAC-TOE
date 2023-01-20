import os
import random
import time
from datetime import date

os.system("clear")

def printHeader():
    print("  --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  ")
    print("|                                                                             |")
    print("|                                 TIC TAC TOE                                 |")
    print("|                                                                             |")
    print("  --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  ")
    print()
    print()

def printChoices():
    print()
    print("Press Key for choices:")
    print("                                  [p]             ->     for Playing game")
    print("                                  [c]             ->     for Credits")
    print("                                  [any other]     ->     for Quiting")
    print()
    print()
    print()

def printThankyou():
    os.system("clear")
    print()
    print()
    print("                        Thank You for playing my game !!")
    print()
    print()
    time.sleep(2)

def printGrid(game_arr):
    print("                                  -------------")
    print("                   (Row) a   ->   | ",game_arr[0][0]," | ",game_arr[0][1]," | ",game_arr[0][2]," |",sep="")
    print("                                  -------------")
    print("                   (Row) b   ->   | ",game_arr[1][0]," | ",game_arr[1][1]," | ",game_arr[1][2]," |",sep="")
    print("                                  -------------")
    print("                   (Row) c   ->   | ",game_arr[2][0]," | ",game_arr[2][1]," | ",game_arr[2][2]," |",sep="")
    print("                                  -------------")
    print("                                    ^   ^   ^")
    print("                              (Col) 1   2   3")
    print()
    

def printTossInformation(player1_name,player2_name):
    print()
    print("We will toss coin to find whether",player1_name,"goes first or",player2_name,"goes first.")
    print()
    print("Press Key for choices:")
    print("                                  [h]              ->     for Heads")
    print("                                  [t]              ->     for Tails")
    print()
    print()

def printTossing(player1_choice,coin,player1_name,player2_name):
    printHeader()
    for i in range(len(player1_name)//2,32):
        print(" ",end="")
    if player1_choice==1:
        print(player1_name," chooses Heads")
    else:
        print(player1_name," chooses Tails")
    print()
    print()
    time.sleep(0.5)
    print("                                 Tossing coin ")
    for i in range(1,11):
        time.sleep(0.5)
        print("                                       .")
    print()
    os.system("clear")
    printHeader()
    for i in range(len(player1_name)//2,28):
        print(" ",end="")
    if player1_choice==coin:
        if coin==1:
            print("It's heads.",player1_name,"goes first!")
        else:
            print("It's tails.",player1_name,"goes first!")
    else:
        if coin==1:
            print("It's heads.",player2_name,"goes first!")
        else:
            print("It's tails.",player2_name,"goes first!")
        
    print()
    print()

    key = input("Press any key to start game: ")

    os.system("clear")
    if player1_choice==coin:
        return 1
    else:
        return 0
    

def toss(player1_name,player2_name):
    os.system("clear")
    printHeader()
    printTossInformation(player1_name,player2_name)
    key = input(player1_name+" calls: ")

    player1_coin_choose = -1

    while key not in ["h","t"]:
        print("Wrong")
        key = input(player1_name+" calls: ")

    if key=='h':
        player1_coin_choose = 1
    elif key=='t':
        player1_coin_choose = 0        

    coin = random.randint(0, 1)
    os.system("clear")
    return printTossing(player1_coin_choose,coin,player1_name,player2_name)    

def printPlayerNamingInformation(num):
    if num==1:
        print("                             Enter name of Player 1")
    else:
        print("                             Enter name of Player 2")
    print()
    print()
    print()

def convert(s):
    return [ord(s[0])-ord('a'),ord(s[1])-ord('1')]

def playerPlay(iteration,game_arr,player1_name,player2_name):
    os.system("clear")
    printHeader()
    printGrid(game_arr)
    print()
    if iteration%2:  
        print(player1_name,"'s turn.                                          ",player1_name,"  -> x")
        for tmp in player1_name:
            print(" ",end="")
        print("                                                   ",player2_name,"  -> o")
    else:
        print(player2_name,"'s turn.                                          ",player1_name,"  -> x")
        for tmp in player2_name:
            print(" ",end="")
        print("                                                   ",player2_name,"  -> o")        
    print()
    print("  Enter two characters(not space-seperated) which denotes row and column names")
    print()

    while True:
        if iteration%2:
            choice_of_player = input(player1_name+": ")
        else:
            choice_of_player = input(player2_name+": ")
        
        check_correct = True
        if choice_of_player not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
            check_correct = False
        else:
            choice_of_player_row,choice_of_player_col = convert(choice_of_player)
            if game_arr[choice_of_player_row][choice_of_player_col] != " ":
                check_correct = False

        if check_correct==False:
            print("Wrong Choice")
        else:
            choice_of_player_row,choice_of_player_col = convert(choice_of_player)
            if iteration%2:
                game_arr[choice_of_player_row][choice_of_player_col] = "x"
            else:
                game_arr[choice_of_player_row][choice_of_player_col] = "o"
            break

    return game_arr


def printPlayerWinner(it,game_arr,player1_name,player2_name):
    os.system("clear")
    printHeader()
    printGrid(game_arr)
    print()
    print()
    if it==1:
        print("                                  ",player1_name,"Wins !!")
    else:
        print("                                  ",player2_name,"Wins !!")

    print()
    print()
    key = input("Press any key to continue: ")
    return

def printPlayerDraw(game_arr,player1_name,player2_name):
    os.system("clear")
    printHeader()
    printGrid(game_arr)
    print()
    print()
    print("                                  Its A Draw !!")
    print()
    print()
    key = input("Press any key to continue: ")
    return   

def playerGame(player1_name,player2_name):
    print()
    print()
    for i in range((len(player1_name)+len(player2_name))//2,33):
        print(" ",end="")
    print("Hello!",player1_name,"and",player2_name)
    time.sleep(1)
    print()
    print()
    print("                                 Let's Play")
    time.sleep(2)
    os.system("clear")
    game_arr = [[" "," "," "],[" "," "," "],[" "," "," "]]
    did_anyone_win = False
    for i in range(1,10):
        game_arr = playerPlay(i,game_arr,player1_name,player2_name)
        r1 = game_arr[0][0]==game_arr[0][1] and game_arr[0][1]==game_arr[0][2] and game_arr[0][0]!=' ' and game_arr[0][1]!=' ' and game_arr[0][2]!=' '
        r2 = game_arr[1][0]==game_arr[1][1] and game_arr[1][1]==game_arr[1][2] and game_arr[1][0]!=' ' and game_arr[1][1]!=' ' and game_arr[1][2]!=' '
        r3 = game_arr[2][0]==game_arr[2][1] and game_arr[2][1]==game_arr[2][2] and game_arr[2][0]!=' ' and game_arr[2][1]!=' ' and game_arr[2][2]!=' '
        c1 = game_arr[0][0]==game_arr[1][0] and game_arr[1][0]==game_arr[2][0] and game_arr[0][0]!=' ' and game_arr[1][0]!=' ' and game_arr[2][0]!=' '
        c2 = game_arr[0][1]==game_arr[1][1] and game_arr[1][1]==game_arr[2][1] and game_arr[0][1]!=' ' and game_arr[1][1]!=' ' and game_arr[2][1]!=' '
        c3 = game_arr[0][2]==game_arr[1][2] and game_arr[1][2]==game_arr[2][2] and game_arr[0][2]!=' ' and game_arr[1][2]!=' ' and game_arr[2][2]!=' '
        d1 = game_arr[0][0]==game_arr[1][1] and game_arr[1][1]==game_arr[2][2] and game_arr[0][0]!=' ' and game_arr[1][1]!=' ' and game_arr[2][2]!=' '
        d2 = game_arr[0][2]==game_arr[1][1] and game_arr[1][1]==game_arr[2][0] and game_arr[0][2]!=' ' and game_arr[1][1]!=' ' and game_arr[2][0]!=' '

        if r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2:
            printPlayerWinner(i%2,game_arr,player1_name,player2_name)
            did_anyone_win = True
            break

    if did_anyone_win == False:
        printPlayerDraw(game_arr,player1_name,player2_name)    
    return

def Player():
    os.system("clear")
    printHeader()
    printPlayerNamingInformation(1)
    player1_name = input("Player 1: ")
    os.system("clear")
    printHeader()
    printPlayerNamingInformation(2)
    player2_name = input("Player 2: ")

    os.system("clear")
    if len(player1_name)==0:
        player1_name="Player 1"
    if len(player2_name)==0:
        player2_name="Player 2"

    ck = toss(player1_name,player2_name)
    
    if ck==1:
        playerGame(player1_name,player2_name)
    elif ck==0:
        playerGame(player2_name,player1_name)


def Credits():
    os.system("clear")
    printHeader()
    print()
    print()
    print("             This game is made by Pratik Tripathy.(@NightFalcon)")
    print()
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("                           The copyright is of",d1[6:])
    print()
    print("                            All Rights Reserved :)")
    print()
    print()
    print()
    print()
    
    k = input("Press any key to get back to main-menu: ")
    return

def game():
    os.system("clear")
    game_on = True

    while game_on:
        os.system("clear")

        printHeader()
        printChoices()
        
        key = input("Choice: ")

        
        if key=='p':
            Player()
        elif key=='c':
            Credits()
        else:
            printThankyou()
            break            

game()
