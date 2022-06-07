for _ in range(int(input())):
    H, W, N = map(int, input().split())
    hotelList = []
    for rooms in range(1, W+1):
        if rooms < 10:
            rooms = "0"+str(rooms)
        for floors in range(1, H+1):
            hotelList.append("{}{}".format(floors, rooms))
    print(hotelList[N-1])
