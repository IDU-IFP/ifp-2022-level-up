# !밀비 급일

# END가 나올떄까지 입력. 입력하는 메세지는 뒤집어 출력
while(1):
    message = input()
    if(message == "END"):
        break
    print(*reversed(message), sep="")