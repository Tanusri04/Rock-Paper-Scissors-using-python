def Gamerules():
    print(''' Hello, welcome to the game of Rock,paper,scissors!
This is a 2 player game where in every turn the player will have to choose between 
rock,paper and scissors. The rules are:
Paper defeats Rock
Scissors defeats Paper
Rock defeats Scissors
If both players choose the same thing, it's a tie
Hope you understood and Enjoy the game!!''')
def Game():
    while True:
        Player1=input("Player 1, its your turn  ")
        Player2=input("Player 2 its your turn  ")
        if Player1=='rock':
            if Player2=='rock':
                print("Draw")
            if Player2=='scissors':
                print("Player 1 wins!")
            if Player2=='paper':
                print("Player 2 wins!")
        if Player1=='scissors':
            if Player2=='scissors':
                print("Draw")
            if Player2=='paper':
                print("Player 1 wins!")
            if Player2=='rock':
                print("Player 2 wins!")
        if Player1=='paper':
            if Player2=='paper':
                print("Draw")
            if Player2=='rock':
                print("Player 1 wins!")
            if Player2=='scissors':
                print("Player 2 wins!")
        print("If you want to play again type 'Yes' else type 'Exit'")
        choice=input()
        if choice=='Yes':
            continue
        else:
            print("Game over, thanks for playing")
            break
Gamerules()
Game()