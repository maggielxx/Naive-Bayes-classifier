#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


import csv


# In[3]:


import numpy as np


# In[4]:


import math


# In[5]:


with open('trg.csv','rt',newline='') as f:
    csv_reader = csv.reader(f,skipinitialspace=True)
    data = list ( csv_reader)


# In[6]:


words = []
for i in range (1, len(data)):
    abstract = data[i][2]
    words_abstract = abstract.split(" ") #Split when there is a space
    words.extend(words_abstract)


# In[ ]:





# In[7]:


k=np.unique(np.sort(words))


# In[8]:


k=np.delete(k,[0,1,3,4])


# In[9]:


wordslist = list (k)


# In[10]:


stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']


# In[11]:


def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


# In[12]:


wordslist=removeStopwords(wordslist, stopwords)


# In[ ]:


def wordListToFreqList(listname,wordlist,wholelist):
    for i in range (1,len(listname)):
        line=listname[i][2].split(" ")
        wordfreq = [line.count(p) for p in wordlist]
        wholelist.append(wordfreq)
    return wholelist


# In[ ]:


wholelist=[]
wholelist.append(wordslist)


# In[ ]:


wordListToFreqList(data,wordslist,wholelist)


# In[ ]:


with open('frelist.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in wholelist:
        writer.writerow(row)


# In[ ]:


#to open the list with frequency


# In[13]:


with open('frelist.csv','rt',newline='') as f:
    csv_reader = csv.reader(f,skipinitialspace=True)
    freq = list ( csv_reader)


# In[14]:


for i in range(len(freq)):
    freq[i].append(data[i][1])


# In[15]:


title=freq[0]


# In[16]:


freq.pop(0)


# In[17]:


random.shuffle(freq)


# In[18]:


subsets = [freq[x:x+400] for x in range(0, len(freq), 400)]


# In[ ]:


with open('subsets.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in subsets:
        writer.writerow(row)


# In[19]:


validset=subsets[0]
trainingset=[]
trainingset=subsets[1]
for i in range(2,10):
    for j in range(0,400):
        trainingset.append(subsets[i][j])


# In[20]:


classlist=[]
for i in range(0,len(trainingset)):
    classlist.append(trainingset[i][-1])
classes=np.unique(classlist)


# In[21]:


def class_prior(listname, typeofclass):
    class_prior = []
    sample_num = float(len(listname))
    for c in typeofclass:
        count=0
        for i in range(len(listname)):
            if listname[i]==c:
                count=count+1
        c_num = count
        class_prior.append(c_num/sample_num)
    return class_prior


# In[22]:


class_prior(classlist,classes)


# In[23]:


def separate_class(c_name,listname):
    separate=[]
    for i in range(len(listname)):
        if listname[i][-1]==c_name:
            separate.append(listname[i])
    separate.append(title)
    return separate


# In[24]:


sep_A=separate_class('A',trainingset)
sep_B=separate_class('B',trainingset)
sep_E=separate_class('E',trainingset)
sep_V=separate_class('V',trainingset)


# In[25]:


def countall(listname,word_num):
    count=0
    for i in range(len(listname)-1):
        for j in range(word_num):
            count=count+int(listname[i][j])
    return count


# In[26]:


word_num=len(wordslist)


# In[27]:


def likeli(word_num, listname,countall):
    attri_prob=[]
    for i in range(word_num):
        count=0
        for j in range(len(listname)-1):
            count=count+int(listname[j][i])
        attri_prob.append((count+0.1)/float(countall+0.1*word_num))
    return attri_prob


# In[28]:


countall_A=countall(sep_A,word_num)


# In[29]:


Likeli_A=likeli(word_num,sep_A,countall_A)


# In[30]:


Likeli_B=likeli(word_num,sep_B,countall(sep_B,word_num))


# In[31]:


countall_E=countall(sep_E,word_num)


# In[32]:


Likeli_E=likeli(word_num,sep_E,countall_E)


# In[33]:


countall_V=countall(sep_V,word_num)


# In[34]:


Likeli_V=likeli(word_num,sep_V,countall_V)


# In[ ]:


def train_one(listname,num):
    prob_A=0
    prob_B=0
    prob_E=0
    prob_V=0
    pre_c=str
    for i in range(0,31957):
        if  int(listname[num][i]) >0:
            prob_A=prob_A+int(listname[num][i])*math.log(Likeli_A[i])
            prob_B=prob_B+int(listname[num][i])*math.log(Likeli_B[i])
            prob_E=prob_E+int(listname[num][i])*math.log(Likeli_E[i])
            prob_V=prob_V+int(listname[num][i])*math.log(Likeli_V[i])    
    max_prob=max(prob_A,prob_B,prob_E,prob_V)
    if max_prob==prob_A:
        pre_c='A'
    elif max_prob==prob_B:
        pre_c='B'
    elif max_prob==prob_E:
        pre_c='E'
    else:
        pre_c='V'
    if listname[num][-1]==pre_c:
        return 1
    else: return 0


# In[ ]:


def train_some(listname):
    right_predict=0
    for j in range(0,len(listname)):
        right_predict=right_predict+train_one(listname,j)
    accuracy=right_predict/float(len(listname))
    return accuracy


# In[ ]:


train_some(validset)


# In[68]:


with open('tst.csv','rt',newline='') as f:
    csv_reader = csv.reader(f,skipinitialspace=True)
    testfile = list ( csv_reader)


# In[40]:


def testFileToFreqList(listname,wordlist,wholelist):
    for i in range (1,len(listname)):
        line=listname[i][1].split(" ")
        wordfreq = [line.count(p) for p in wordlist]
        wholelist.append(wordfreq)
    return wholelist


# In[41]:


splitTest=[]


# In[42]:


testFileToFreqList(testfile,wordslist,splitTest)


# In[ ]:


with open('splittotest.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in splitTest:
        writer.writerow(row)


# In[43]:


def test_one(listname,num):
    prob_A=0
    prob_B=0
    prob_E=0
    prob_V=0
    pre_c=str
    for i in range(0,31975):
        if  int(listname[num][i]) >0:
            prob_A=prob_A+int(listname[num][i])*math.log(Likeli_A[i])
            prob_B=prob_B+int(listname[num][i])*math.log(Likeli_B[i])
            prob_E=prob_E+int(listname[num][i])*math.log(Likeli_E[i])
            prob_V=prob_V+int(listname[num][i])*math.log(Likeli_V[i])    
    max_prob=max(prob_A,prob_B,prob_E,prob_V)
    if max_prob==prob_A:
        pre_c='A'
    elif max_prob==prob_B:
        pre_c='B'
    elif max_prob==prob_E:
        pre_c='E'
    else:
        pre_c='V'
    return pre_c


# In[73]:


def test_some(listname,lastfile):
    for j in range(0,len(listname)):
        class_value=test_one(listname,j)
        lastfile[j+1][1]=class_value


# In[71]:


testfile[0][1]='class'


# In[74]:


test_some(splitTest,testfile)


# In[77]:


with open('xliu404.csv', 'w', newline='') as csvfile:
    writer  = csv.writer(csvfile)
    for row in testfile:
        writer.writerow(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




