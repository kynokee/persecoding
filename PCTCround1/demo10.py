icecream = input()
I = 0
M = 0
C = 0

for i in icecream:
    if i == 'I':
        I += 1
    elif i == 'M':
        M += 1
    elif i == 'C':
        C += 1

if I < 2:
    print("I")
elif M < 1:
    print("M")
elif C < 3:
    print("C")
