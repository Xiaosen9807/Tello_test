#Programmer: Qin Xusen
#Time: 2021/4/28-17:39
f=[]
for i in range(100,1000):
    if (i//100)**3+((i-100*(i//100))//10)**3+(i%10)**3==i:
       f.append(i)
    else:
        continue
print(','.join(str(i)for(i)in (f)))