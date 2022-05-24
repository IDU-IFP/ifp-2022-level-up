count = 0

str = input()
listAlpha = list(str)

for i in listAlpha:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print(count)
