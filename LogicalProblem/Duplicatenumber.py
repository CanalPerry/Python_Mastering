def findeduplicatenumber(list):
    const = True
    duplicate = 0
    while const == True:
        for i in range(0, len(list)):
            for v in range(1, len(list)-1):
                if list[i] == list[v]:
                    duplicate = list[v]
                    const = False
                    break
            if const == False:
                break
    return duplicate
print(findeduplicatenumber([1,3,3,4,5,6]))