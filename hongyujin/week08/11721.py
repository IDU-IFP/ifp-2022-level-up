n = input()
for i in range(0, len(n), 10):  # 10칸격으로 ex 1을 입력 받으면 11받고  21받고...
    print(n[i:i+10])   # i 부터 i +9까지
