#Programmer: Qin Xusen
#Time: 2021/4/27-11:36
def rvs(s):
    if s=='':
        return s
    else:
        return rvs(s[1:])+s[0]
print(rvs('apple'))