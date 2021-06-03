#Programmer: Qin Xusen
#Time: 2021/4/27-11:41
def F(n):
    if n==1 or n==2:
        return 1
    else:
        return F(n-1)+F(n-2)

print(F(9))
