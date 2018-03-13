def mars_calc(str) :
    tlist = str.split()
    num = float(tlist[0])
    tlen = len(tlist)
    for i in range(1,tlen) :
        if tlist[i] == '@':
            num *=3
        elif tlist[i] == '%' :
            num += 5
        elif tlist[i] == '#' :
            num -= 7
    return num
            
t  = int(input())
for i in range(t) :
    tmp = input()
    print("%.2f" % (mars_calc(tmp)))