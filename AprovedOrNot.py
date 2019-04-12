#a program that reads the note of a studend and if is greater than 6, returns approved else desapproved.

def consult(n):
    if n >= 6:
        print ('Approved')
    else:
        print ('Desapproved')

note = int(input("What is the note of the student: "))
consult(note)

