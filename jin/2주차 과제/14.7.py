a, b, c, d = map(int, input().split())

if 0<a<101 and 0<b<101 and 0<c<101 and 0<d<101 :
    
    if (a+b+c+d)/4 >= 80 :
        print('합격')
    else :
        print('불합격')
        
else:
    print('잘못된 점수')