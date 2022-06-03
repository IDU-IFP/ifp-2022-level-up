k = int(input())
mat = []
for j in range(1, k+1):
    mat = list(map(int, input().split()))
    mat = mat[1:]
    s_student = sorted(mat)
    lg = 0    # 가장 큰 점수 차이
    for i in range(len(s_student)-1):     # len -> 초기값 1, 2일때
        if s_student[i+1] - s_student[i] > lg:
            lg = s_student[i+1] - s_student[i]
    print('Class {}'.format(j))  # print(f'Class {j}')
    print(f'Max {max(s_student)}, Min {min(s_student)}, Largest gap {lg}')
