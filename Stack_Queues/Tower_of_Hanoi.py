def solve(n):
    if n<=0:
        return None

    srcTower=[i for i in range(1,n+1)]
    destTower=[]
    buffTower=[]

    def move(q,src,dest,buffer):
        if q<=0:
            return
        move(q-1,src,buffer,dest)
        dest.append(src.pop())
        move(q-1,buffer,dest,src)

    move(n,srcTower,destTower,buffTower)
    print(srcTower,destTower)

solve(100)
