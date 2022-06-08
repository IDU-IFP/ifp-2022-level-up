croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in croatia:
    s = s.replace(i, 'a')  # replace 함수를 이용하여 문자열을 변경
    # 바꿀 문자열 = a
print(len(s))
