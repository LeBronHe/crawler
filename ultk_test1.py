# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:15:32 2018

@author: Administrator
"""

import nltk
#nltk.download()





from nltk.book import * 

text1.concordance("monstrous") #搜索单词，并显示上下文
text1.similar("monstrous") #搜索具有相似上下文的单词
text2.common_contexts(["monstrous","very"]) #两个或两个以上的词的共同的上下文
sorted(set(text3)) #筛重
text3.count("smote")
text3.generate() # 根据语料3的词序列统计信息生成随机文本

sent1=['Call', 'me', 'Ishmael', '.']
sent4+sent1
sent1.append("Some")
text1[2] #文本第2个词
text4.index('awaken') #索引
text1[2:5]
'对字符串也能切片，*，+等'
' '.join(['Monty','Python'])
'Monty Python'.split()

'找文本中出现频率最高的50个词'
from nltk.book import *
fdist1=FreqDist(text2)


'该方法接受一个数字n作为参数，会以表格的方式打印出现次数最多的前n项。'
fdist1.tabulate(15)

'该方法接受一个数字n作为参数，返回出现次数最多的前n项列表。'
fdist1.most_common(15)

'该方法会返回一个低频项列表，低频项即出现一次的项。'
fdist1.hapaxes()

'返回出现次数最多的项。'
print(fdist1.max())

fdist1.plot(50,cumulative=True) #画图

'中文可设置为大于1？排除一个字的词'
v=set(text1)
long_words=[w for w in v if len(w)>15]
long_words

'长度超过7次，出现超过7次的词'
fdist5=FreqDist(text5)
sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7])

'找双连词，如：four years'
text4.collocations()

'查看词长的分布'
[len(w) for w in text1]
'该词长的出现频率'
fdist=FreqDist([len(w) for w in text1])
fdist.keys()
fdist.items()
fdist.max()
fdist.freq(3)
fdist.N() #样本总数

'原字符中的一部分，在开头、结尾、中间，以及判断所有大写小写？字母？数字？首字母大写'
sorted([w for w in set(text1) if w.endswith('ableness')])#以ablenss结尾的词
sorted([w for w in set(text4) if 'gnt' in w])#包含’gnt‘

'古藤保语料库'
nltk.corpus.gutenberg.fileids()

from nltk.corpus import gutenberg
gutenberg.fileids()

emma=gutenberg.words('austen-emma.txt')

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid)) #原始文本的字符的长度
    num_words=len(gutenberg.words(fileid))  #词的长度
    num_sents=len(gutenberg.sents(fileid)) #划为句子长度
    num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)
#平均词长，平均句子长，每个词出现的平均次数

'加载自己的语料库'
from nltk.corpus import PlaintextCorpusReader
corpus_root='E:/python shell'
wordlists=PlaintextCorpusReader(corpus_root,'.*')
wordlists.fileids()

ll=wordlists.words('items1.txt')
wordlists.sents('items1.txt')

'过滤停用词，让原来的表不出现停用词表中出现的词'
from  nltk.corpus import stopwords
stopwords.words('english')

def content_fraction(text):
    stopwords=nltk.corpus.stopwords.words('english') #加载自己的停用词库就不用这句了
    content=[w for w in text if w.lower() not in stopwords]
    return content
'过滤了停用词，有必要的话，可以用同义词表'


'中文测试'
import pandas as pd
import jieba
import re
from nltk.book import *
from nltk.corpus import PlaintextCorpusReader
import nltk
import jieba.posseg as pseg

df=pd.read_table('E:/python shell/tutorial/items1.txt')
df2= df['txt'].map(lambda x:' '.join(jieba.cut(x)))
#for ele in df2:  
    #if ele.flag == 'nr' or ele.flag == 'ns' or ele.flag == 'nt' or ele.flag == 'nz':  
    #print(ele.flag)
#english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']

#df2.to_csv('E:/python shell/tutorial/jieba.txt')

corpus_root='E:/python shell'   #/tutorial'
wo=PlaintextCorpusReader(corpus_root,'.*')
wo.fileids()


df3=[w for w in df2 if w not in wo.words('stopwords1893.txt')] #stopwords1893 1229

#dd=re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）]+|+","",str(df3))#去掉中英文符号
df4=[w for w in df3 if w not in nltk.corpus.stopwords.words('english')]
#去除标点符号  
punctuations = ['。"','/','','?',',','_','-','?','“','"',':','：',',','，','。','；',';', '.', ':',',', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%'] 

df5=[w for w in df4 if w not in punctuations]


df6=pd.DataFrame(columns=None,data=df5)
df6.to_csv('E:/python shell/tutorial/df6.txt',encoding = "utf-8")


'标注汉语词性'
import nltk
text=nltk.word_tokenize("And he fuck you completely different")
nltk.pos_tag(text)

from nltk.corpus import sinica_treebank #中文标注库

import jieba
import jieba.posseg as pseg
import time
import sys

t1=time.time()
f=open("E:/python shell/tutorial/df6.txt","r",encoding = "utf-8") #读取文本
string=f.read()
words = pseg.cut(string) #进行分词

result="" #记录最终结果的变量
for w in words:
    if w.flag == 'n' or w.flag == 'eng' and w.word !=' ':
        result+=str(w.word)+'\n' #加词性标注
f=open("E:/python shell/tutorial/jieba2.txt","w",encoding = "utf-8") #将结果保存到另一个文档中
f.write(result)
f.close()
t2=time.time()
print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果


'加载jieba2.txt'
from nltk.corpus import PlaintextCorpusReader
corpus_root='E:/python shell/tutorial'
data=PlaintextCorpusReader(corpus_root,'.*')
data.fileids()
ll=data.words('jieba2.txt') #加载前txt格式转为‘utf-8’

lll=[w for w in ll if w not in punctuations]

#去停用词
ll2=[w for w in lll if w not in wo.words('stopwords1893.txt')] #stopwords1893 1229
ll3=[w for w in ll2 if w not in nltk.corpus.stopwords.words('english')]
ll4=[w for w in ll3 if  not w.isdigit()] #去掉数字
ll5=[w.lower() for w in ll4] #将英文小写
ll6=nltk.pos_tag(ll5) #标注英文
ll7=[]
for i in range(len(ll6)):
    if ll6[i][1]=='NN' or ll6[i][1]=='NNP':
        ll7.append(ll6[i][0])



'''
text = open("E:/python shell/tutorial/df6.txt", 'r', encoding='utf-8').read() # 读取文本内容
fredist = nltk.FreqDist(text.split(' ')) # 获取单文件词频
'''

#fd=sorted([w for w in set(ll2) if len(w)>2 ])

fdist5=FreqDist(ll7)
fdist5.most_common(30)

'1.英文大小写变换'
'2.提取名词（中英文）'
'3.同义词转换'
'4.中文分词'
'5.去停留词，去标点符号'

'信息提取中，需要对文本进行分块，在分块后将名词、动词等存到一张表中，用sql来查询，如：贵州豆腐很好吃，...，则将词句分为一个块（根据词性），提取贵州，豆腐，很好吃'
'要识别文本中的地点名词或实体名词咋办？用语料库如果不同的国家容易错，一些新出的词也不容易识别，英文中nltk提供nltk.ne_chunk(txt,binary=True)来标注为NE'
'自然语言的理解，是将问的话转为sql（英文是sq10.fcfg），然后在数据库中查找答案'

import  nltk
from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'What cities are located in China'#'What cities are located in China'
trees = next(cp.parse(query.split()))
answer =trees.label()['SEM']
p=str(answer).replace(',','').replace('(','').replace(')','')
print(p)


from nltk.sem import chat80
rows=chat80.sql_query('corpora/city_database/city.db',p)
for r in rows:
    print(r[0])
 
'用另一库提取关键字'
import pynlpir
pynlpir.open()
s ='怎么才能把电脑里的垃圾文件删除'
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print(key_word[0],'\t', key_word[1])
    pynlpir.close()




