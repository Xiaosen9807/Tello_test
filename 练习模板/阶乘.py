def cmul(a):
    s=[]
    l=a.split(sep=',')
    print(l)
    for i in l:
        s.append(int(i))
    result=1
    for x in s:
        result*=x
    return result



m=input()
print(eval("cmul(m)"))

#print(eval("cmul({})".format(input())))