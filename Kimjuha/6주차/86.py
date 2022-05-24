w, h, b = map(int, input().split())
result = (w*h*b)/(8*1024**2)
print(round(result, 2), 'MB')
