def logic(i):
    return {"c=": 1, "c-": 1, "dz=": 1, "d-": 1, "lj": 1, "nj": 1, "s=": 1, "z=": 1}.get(i, 0)


count = 0
croString = input()
listString = list(croString)

while(1):
    if len(listString) != 0:
        if logic("".join(listString[0:2])) == 1:
            joinString = "".join(listString[0:2])
            count += logic(joinString)
            del listString[0:2]
        elif logic("".join(listString[0:3])) == 1:
            joinString = "".join(listString[0:3])
            count += logic(joinString)
            del listString[0:3]
        else:
            count += 1
            del listString[0:1]
    else:
        break
print(count)
