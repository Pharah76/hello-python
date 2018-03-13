chour, cmin, csec = map(int, input().split())
asec = int(input())
semi_r = chour*3600+cmin*60+csec+asec
limit = 24*3600


while semi_r >= limit :
    semi_r -= limit
print("%d %d %d" % (semi_r/3600, (semi_r%3600)/60, (semi_r%3600)%60))