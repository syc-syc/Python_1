#2단 - 9단

dan = 0
print("구구단")

for i in range(2,10,1):
    print("==%d단=="%i)
    for j in range(1,10,1):
        dan=i*j
        print("%2d * %2d = %2d"%(i,j,dan))
        



