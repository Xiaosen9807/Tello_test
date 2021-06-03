#Programmer: Qin Xusen
#Time: 2021/4/28-22:58
def getNum():  # 获取用户不定长度的输入
    numbers=[]
    l=input().split(sep=',')
    for i in l:
        numbers.append(float(i))
    return numbers
    mean(numbers)
    dev(numbers,mean(numbers))
    median(numbers)


def mean(numbers):  # 计算平均值
    Total=0
    for i in numbers:
        Total+=i
    mean=Total/int(len(numbers))
    return mean


def dev(numbers, mean):  # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    numbers.sort(reverse=True)
    l=int(len(numbers))
    if l%2!=0:
        return int(numbers[int(l/2)])
    else:
        return (numbers[int(l/2)]+numbers[int(l/2-1)])/2





n = getNum()  # 主体函数
m = mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(mean(n),dev(n,m),median(n)))