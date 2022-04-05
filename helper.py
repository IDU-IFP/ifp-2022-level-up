# num = 5
# count = 1
# flag = 1
# arr = [[0] * num for _ in range(num)]
# x, y = 0, 0
# for i in range(num):
#     arr[y][x] = count;
#     count += 1
#     x += flag
# x -= 1

# for j in range(num-1, 0, -1):
#     for k in range(j):
#         y += flag
#         arr[y][x] = count;
#         count += 1
#     flag *= -1
#     for l in range(j):
#         x += flag
#         arr[y][x] = count;
#         count += 1
        
# for _ in range(num):
#     for i in range(num):
#         print(arr[_][i],end=" ")
#     print(" ")
#HELLO