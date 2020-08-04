# -*- coding: utf-8 -*-
"""3_Co_occurrence

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HSgUpl97trXgaL476Kg7IL9zMy5Zyjfg

# Co-occurrence matrix
특정 단어와 다른 단어의 동시 출연 횟수를 카운트하여 분석
"""

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

docs = ['성진과 창욱은 야구장에 갔다',
        '성진과 태균은 도서관에 갔다',
        '성진과 창욱은 공부를 좋아한다']

count_model = CountVectorizer(ngram_range=(1,1))
x= count_model.fit_transform(docs)

print(count_model.vocabulary_)

# co-cocurrence 행렬 조회
print(x)

print(x.toarray(),'\n')
print(x.T.toarray())

xc = x.T*x
xc.setdiag(0)
print(xc.toarray())

count_model = CountVectorizer(ngram_range=(1,2))
x = count_model.fit_transform(docs)

print(count_model.vocabulary_)
print(x)

xc = x.T * x
xc.setdiag(0)
print(xc.toarray())

C = xc.toarray()

U, S, VT = np.linalg.svd(C, full_matrices = True)
print(np.round(U, 2), '\n')
print(np.round(S, 2), '\n')
print(np.round(VT, 2), '\n')

U.shape

s = np.diag(S)
print(np.round(s,2))

from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(n_components =4, n_iter=13)
D = svd.fit_transform(xc.toarray())

U = D / svd.singular_values_
S = np.diag(svd.singular_values_)
VT = svd.components_

print(np.round(U, 2), '\n')
print(np.round(S, 2), '\n')
print(np.round(VT, 2), '\n')

print(svd.singular_values_)