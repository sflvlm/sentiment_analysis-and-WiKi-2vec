import codecs,sys

f = codecs.open('zhwiki-latest.txt','r',encoding='utf8')
line = f.readline()
print(line)