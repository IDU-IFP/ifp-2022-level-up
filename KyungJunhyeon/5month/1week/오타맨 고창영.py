import string


for i in range(int(input())):
    messageList = []
    index, message = map(str, input().split())
    index = int(index)
    messageList = list(message)
    del messageList[index-1]
    print(''.join(messageList))
