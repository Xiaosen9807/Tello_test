#Programmer: Qin Xusen
#Time: 2021/5/4-11:02
from PyPDF2 import PdfFileReader, PdfFileMerger
merger=PdfFileMerger()
input1=open('document1.pdf','rb')
input2=open('document2.pdf','rb')
merger.append(fileobj=input1,page=(0,3))
merger. merger(position=2,fileobj=input2,pages=(0,1))
output=open("document-output.pdf","wb")
merger.write(output)

