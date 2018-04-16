import jieba
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


f=open('page_data.json')
dic=json.load(f)
corpus=[]
for i in range(len(dic)):
    i+=1
    seg_list=jieba.cut(dic[str(i)],cut_all=False)
    corpus.append(' '.join(seg_list))
    print(len(corpus))
vectorizer = CountVectorizer()
'''词频矩阵X[i][j]表示j词在第i个文本的词频'''
X = vectorizer.fit_transform(corpus)
# 02、构建TFIDF权值
transformer = TfidfTransformer()
# 计算tfidf值
tfidf = transformer.fit_transform(X)
# 03、获取词袋模型中的关键词
word = vectorizer.get_feature_names()
# tfidf矩阵
weight = tfidf.toarray()
print(weight.shape)
np.savetxt('weight_range.txt',weight)