word = input()
wordlength = 0

for i in word:
    wordlength += 1

w = ''
wlength = 0

while wlength <= 30:
    w = w + word
    wlength = wlength + wordlength

print(w)
