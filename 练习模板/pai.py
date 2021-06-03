#Programmer: Qin Xusen
#Time: 2021/4/28-17:22
import random
from time import time

n=int(input('次数'))
sum=0
start=time() #计时开始
random.seed(123)
for i in range(1,n):        #蒙特卡洛法计算圆周率
    a = random.random()
    b = random.random()
    if (a**2+b**2)**0.5<1:
        sum+=1
    else:
        continue
pai=4*sum/n
Time_used=(time()-start) #结束时间减去开始时间
print('%.6f' % pai)
print('The time used by wunning the program is:{}'.format(Time_used))