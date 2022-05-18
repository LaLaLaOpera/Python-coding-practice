def solution(record):
    newList=[]
    printList=[]
    for i in record:
        newList.append(i.split())
    for i in range(len(newList)):
        if len(newList[i]) == 3:
            for j in range(len(newList)-1, -1,-1):
                if len(newList[j]) == 3:
                    if newList[i][1] == newList[j][1] and newList[i][2] != newList[j][2]:
                        newList[i][2] = newList[j][2]
    for i in range (len(newList)):
        if len(newList[i]) == 2:
            for j in range (len(newList)-1, -1, -1):
                if newList[i][1] == newList[j][1]:
                    newList[i].append(newList[j][2])
    for i in range (len(newList)):
        if newList[i][0] == "Change":
            for j in range(len(newList)):
                if newList[j][1] == newList[i][1]:
                    newList[j][2] = newList[i][2]
    for i in range (len(newList)):
        if newList[i][0] == "Enter":
            printList.append(newList[i][2]+"님이 들어왔습니다.")
        elif newList[i][0] == "Leave": 
            printList.append(newList[i][2]+"님이 나갔습니다.")
    print(printList)
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
