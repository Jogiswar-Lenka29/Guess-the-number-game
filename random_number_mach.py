import random
RN= random.randint(100,999);print("Wllcom to our guessing number game")
print(RN)
guess=int(input("Enter a three digit number for match it(For quite press 5)"))
while guess!=5:
    temp1=RN
    temp2=guess
    while RN>=0:
        tempI=temp1%10
        tempII=temp2%10
        if temp1==temp2:
            print('''Congurates!
            man danm how did tou guessed the coreect number ''')
        if tempI==tempII:
            i=1
            print("%i digits were guessed correct"%i)
            i+=1
    else :
        guess=int(input("try again with another 3 digit number"))
else :
    print("You have quited the guessing number game")
    