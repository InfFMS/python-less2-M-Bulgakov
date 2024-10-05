k1 = [int(input()),int(input())]
k2 = [int(input()),int(input())]
t1  = [k1[0]-1,k1[1]-2]
t2  = [k1[0]-2,k1[1]-1]
t3  = [k1[0]-2,k1[1]+1]
t4  = [k1[0]-1,k1[1]+2]
t5  = [k1[0]+1,k1[1]+2]
t6  = [k1[0]+2,k1[1]+1]
t7  = [k1[0]+2,k1[1]-1]
t8  = [k1[0]+1,k1[1]-2]
if k2 == t1 or k2 == t2 or k2 == t3 or k2 == t4 or k2 == t5 or k2 == t6 or k2 == t7 or k2 == t8:
    print('YES')
else:
    print('NO')