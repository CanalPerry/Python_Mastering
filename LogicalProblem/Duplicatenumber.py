def findeduplicatenumber(list):
    a = 0
    b = 0
    duplicate = None
    for i in range(0, len(list)):
        for v in range(0, len(list)):
            a = list[i]
            b = list[v]
            if a == b and i != v:
                duplicate = list[v]
                break
            b = 0
    if duplicate != None:
        return duplicate
    else:
        print("Not exist duplicate number.")
        return duplicate
lista = [1,2,3,4]
print(findeduplicatenumber(lista))