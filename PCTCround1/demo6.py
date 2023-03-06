names = []

for i in range(5):
    names.append(input())

place = 1

for i in names:
    if i == "Ellie":
        break
    else:
        place = int(place) + 1

if int(place) == 1:
    print('1st')
elif int(place) == 2:
    print('2nd')
elif int(place) == 3:
    print('3rd')
elif int(place) == 4:
    print('4th')
else:
    print('5th')
