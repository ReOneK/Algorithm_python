def hut(n,x,y,z):
    if n==1:
        print(x,"-->",z)
    else:
        hut(n-1,x,z,y)     #将n-1个盘子从x移动到y
        print(x,"-->",z)   #将最后一个盘子从x移动到z
        hut(n-1,y,x,z)     #将 y上的n-1个盘子移动到z


n=int(input("please input a number:"))

b=hut(n,"x","y","z")
