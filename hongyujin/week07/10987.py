word = input()
vowel = 'aeiou'
res = 0
for i in vowel:
    res += word.count(i)    # count()함수를 이용하여 word에 있는
    # 모음의 개수를 센 후 res에 더한다
print(res)
