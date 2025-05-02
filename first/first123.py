from  random import randint
num=randint(1,10)
print("Try and guess the number between 1 and 10")

x=0

for x in range(3):
    guess=int(input("Type a number between 1 an 10 :"))
    print(guess)
    if guess==num:
        print("Good job you got  it")
        break
    elif guess!=num and x<3:
        print("Wrong answer try again")
    else:
        print("The correct answer was",num)


