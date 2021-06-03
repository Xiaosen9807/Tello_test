#Programmer: Qin Xusen
#Time: 2021/4/14-10:52

def getText():
    txt=open("C:\\Users\\Surface\\Desktop\\hamlet.txt","r").read()
    txt=txt.lower()
    for i in '|"$%&()+,-./:;<=>?@{\\}^_‘{|}~':
        txt=txt.replace(i," ")
    return txt



hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
print(items)
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    (word,counts)=items[i]
    print("{0:<10}{1:<50}".format(word,counts))
