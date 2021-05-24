# By Mahendrakumar Murugesan I know this code is Silly but it ok
# Date : 14.10.2020
# Time : 9.57.44 PM
# Name of The Project : Hangman Project
import random
print('*** WELCOME TO HANGMAN ***')
print('HangMan life is in Your Hands')
name = input("Enter Your Name: ")
print("  ")
print("  ")
print('Welcome To Hangman Game ' + name)
tur_no = 15
points = 0


def Main(A,B,C,D,E):
    aans = 'sea'
    bans = "netflix"
    cans ='laptop'
    dans ='bike'
    eans = "sun"

    points = 0
      
    if A== aans:
        print('The answer is Correct')
        points = points+1
    else:
        print(" Wrong!!!!the answer is " +aans)
    if B== bans:
        print('The answer is Correct')
        points = points+1
    else:
        print(" Wrong!!!!the answer is " + bans)
    if C== cans:
        print('The answer is Correct')
        points = points+1
    else:
        print(" Wrong!!!!the answer is " + cans)         
    if D == dans:
        print('The answer is Correct')
        points = points+1
    else:
        print(" Wrong!!!!the answer is " +dans)
    if E == eans:
        print('The answer is Correct')
        points = points+1
    else:
        print(" Wrong!!!!the answer is " +eans)

     
    print("YOUR SCORE is" + str(points))


    if points < 0:
        print("YOu LOse")
        print("The HangMan Is Angey With You")
    elif points > 0:
        print("good try DuDe")
        print("The Hangman is Very TO Have a friend Like you")
    else:
        print("NotHing To say")    
        


A = input("World's Biggest water source ?")
B = input("The Biggest OTT platform? ")
C = input("It is a Notebook Computer? ")
D = input("It has 2 Wheelar.It a Veichle")
E = input("Biggest Energy Source")
Main(A,B,C,D,E)