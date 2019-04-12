#write a program that returns a new balance of an application that improves 1%

def improve(n):
    nb = n * 1.01
    return nb

application = float(input("Enter with your money: $"))
newbalance = improve(application)

print (f'Your new balance is ${newbalance}')