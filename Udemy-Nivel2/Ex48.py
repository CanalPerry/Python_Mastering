# EX-48

def fibonnaci():
    fibolist = [0, 1]
    l1 = 0
    l2 = 1
    soma = 0
    fim = 4000000000
    const = True
    while(const == True):
        while(fibolist[l2] <= fim):
            r = fibolist[l1] + fibolist[l2]
            fibolist.append(r)
            l1 += 1
            l2 += 1
            if(fibolist[l2] % 2 == 0):
                soma += fibolist[l2]
        const = False
    print(soma)
    print(fibolist)
fibonnaci()