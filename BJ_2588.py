# input은 입력되는 모든 것을 문자열로 취급한다.
a = int(input())
b = input()

#print(a[0], a[1], a[2])

m1 = a*int(b[2])
m2 = a*int(b[1])
m3 = a*int(b[0])

print(m1)
print(m2)
print(m3)
print(m1+m2*10+m3*100)