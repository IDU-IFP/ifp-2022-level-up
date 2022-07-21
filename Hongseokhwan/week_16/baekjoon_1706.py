# 크로스워드

puzzle = [] # 퍼즐판
r,c = map(int,input().split()) # 퍼즐판 크기
save_arr = [] # 값을 임시 저장하는 배열
word = "" # 세로 단어를 저장하기 위한 변수
col_arr = [] # 세로 단어
row_arr = [] # 가로 단어

for i in range(r): # 퍼즐 줄 수 만큼 반복
    line = input() # 퍼즐 한줄 입력 후
    puzzle.append(line) # 퍼즖판에 저장
    save_arr.extend(line.split('#')) # 암사 저장 배열에 #로 구분한 값들 저장

for i in save_arr: # 임시 저장 배열에서
    if(len(i) > 1): # 문자열 길이가 2 이상인 요소만
        row_arr.append(i) # 가로 단어 배열에 추가

# 세로 단어 구하는 반복문
for i in range(c): 
    for j in range(r): 
        if(puzzle[j][i] != '#'): # 해당 문자가 #이 아니라면
            word += puzzle[j][i] # word 에 추가
        else: # #이라면
            if(len(word) > 1): # word에 저장된 문자열 길이가 2 이상이라면
                row_arr.append(word) # 세로 단어 배열에 추가 후
                word = "" # word 값 초기화
            else: # 2 미만이라면
                word = "" # 추가 없이 word 값 초기화
        if(j == r-1): # 퍼즐판의 마지막 줄 문자라면
            if(len(word) > 1): # word에 저장된 문자열 길이가 2 이상이라면
                row_arr.append(word) # 세로 단어 배열에 추가후
                word = "" # word 값 초기화
            else: # 2 미만이라면
                 word = "" # 추가 없이 word 값 초기화 후 다음 세로줄로 이동

col_arr.sort() # 가로 단어 배열 정렬
row_arr.sort() # 세로 단어 배열 정렬

if(not row_arr): # 세로 단어가 없다면
    print(col_arr[0]) # 가로 단어의 첫번째 요소 출력
elif(not col_arr): # 가로 단어가 없다면
    print(row_arr[0]) # 세로 단어의 첫번째 요소 출력
else: # 세로 단어, 가로 단어가 1개 이상 있는 경우
    if(row_arr[0] > col_arr[0]): # 세로 단어의 첫번째 요소가 더 크다면
        print(col_arr[0]) # 가로 단어의 첫번째 요소 출력
    else: # 아니라면
        print(row_arr[0]) # 세로 단어의 첫번째 요소 출력