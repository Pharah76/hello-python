t = int(input())
mat = [[int(x) for x in input().split()]for y in range(t)]
for i in range(t):
    print("Case #%d: %d" % (i+1, mat[i][0]+mat[i][1]))