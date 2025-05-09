balance = 100

print("what you like to deposit or withdraw:")
operation=input()

if operation== "deposit":
    print("How much would you like to deposit:")
    depo = int(input())
    newbalance=depo+balance
    print("You know have ",newbalance,"in youre acount")
    
if operation== "withdraw":
    print("How much would you like to withdraw:")
    withdraw = int(input())
    if withdraw>balance:
        print("You don't have enough money")
    else:
        newbalance=balance-withdraw
        print("You know have ",newbalance,"in youre account")