# 5800번 성적 통계
student = []
for j in range(1,int(input())+1):
    student = list(map(int,input().split()))
    student = student[1:]
    score = sorted(student)
    Lgap = 0
    for i in range(0,len(score)-1): 
        if score[i+1] - score[i]>Lgap:
            Lgap = score[i+1] - score[i]
    print(f'Class {j}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {Lgap}')