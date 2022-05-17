char = input()

for i in range(1, 16):
    print('%s*%s=%s' % (char, hex(i)[2:].upper(), hex(int(char, 16)*i)[2:].upper())
