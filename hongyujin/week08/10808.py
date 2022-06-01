s = input()
arr = [0]*26  # 알파벳 a ~ z까지 총 26개이므로 초기화해준다
for i in s:
    arr[ord(i) - 97] += 1  # 배열 안에서 소문자 a를 주면 0번지 값 a, 1번지 b
    # 같은 알파벳의 개수가 알고 싶어서 1씩 계속 더해줌
for i in arr:              # 전체를 출력하기 위해서
    print(s[i], end=' ')
