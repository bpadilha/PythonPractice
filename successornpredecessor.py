#return the successor and predecessor of a number

def successor(n):
    nsuc = n + 1
    return nsuc

def predecessor(n):
    npred = n - 1
    return npred

number = int(input("Write a number: "))

print (f'The successor is {successor(number)} and predecessor is {predecessor(number)}')