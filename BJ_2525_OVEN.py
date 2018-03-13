chour, cmin = map(int, input().split())
amin = int(input())
limit = 24*60
semi_result = chour*60+cmin+amin

if semi_result >= limit :
    semi_result -= limit
    
print("%d %d" % (semi_result/60, semi_result%60))