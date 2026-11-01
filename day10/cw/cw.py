A = 0
while A != 20:
    print(A)
    A += 1

B = 20
while B > 0:
    print(B)
    B -= 1

C = 0
while C != 50:
    print(C)
    C += 2

D = 20
while D > 0:
    print(D)
    D -= 3

password = "Goal-oriented academy"
guess = input("please enter password: ")
while password != guess:
    guess = input("please enter password: ")
print("correct password")
