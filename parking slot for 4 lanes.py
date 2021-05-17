def returnMaxFreeSlotsLane(free_slots):
    lane_no=1
    free=free_slots[1]
    for i in range(2,5):
        if(free<free_slots[i]):
            free=free_slots[i]
            lane_no=i
    return lane_no

lane=["T","A","B","C","D"]
parked_car=[]
free_slots=10*[5]
free_slots[0]=0
for i in range(1,5):
    booked_slots=input().split(",")
    if(booked_slots[0]!='-1'):
        booked=len(booked_slots)
        free_slots[i]=10-booked
waiting_cars=int(input())
if(sum(free_slots)<waiting_cars):
    print("X")
else:
    while(waiting_cars!=0):
        lane_no=returnMaxFreeSlotsLane(free_slots)
        booked=10-(free_slots[lane_no])
        while(waiting_cars!=0 and booked !=10):
            booked+=1
            parked_car.append(lane[lane_no] + str(booked))
            waiting_cars-=1
        free_slots[lane_no]=10-booked
    for book in parked_car:
        print(book,end=' ')
