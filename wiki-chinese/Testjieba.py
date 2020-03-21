import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs,sys

def cut_words(sentence):
    return " ".join(jieba.cut(sentence)).encode('utf-8')

f = codecs.open('iki_zhs.text','r',encoding='utf8')
target = codecs.open('zh.jian.wiki.seg.txt','w',encoding='utf8')
print('openfiles')
line_num = 1
line = f.readline()
while line:
    print('-----processing  ',line_num,' article-------')
    line_reg = " ".join(jieba.cut(line))
    target.writelines(line_reg)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()
exit()