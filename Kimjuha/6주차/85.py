h, b, c, s = map(int, input().split())

result = h*b*c*s
resultMB = result/(8*1024**2)
print(round(resultMB, 1), 'MB')
