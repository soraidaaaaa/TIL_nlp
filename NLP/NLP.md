# NLP

## WordEncoding

단순 수치화를 통해 방법론적으로 빈도기반(통계적 기반)의 분석을 진행한다.

### TF - IDF

빈도를 기반 하여 중요도 및 유사성을 판단한다

Term 과 Documents (term 으로 이루어진 문서) 를 비교할 때

DF (document frequency): DF 가 높은 단어는 여러 documents 에서 자주 사용되었다는 것을 의미한다 (즉 general 한 term = 중요도가 낮을 확률 이 높다)

> 단어의 중요도 ∝ 1/Df ∝ TF



TF = Term-Document Matrix 에서 해당 documents 에서 term 이 나올 확률

IDF = log(documents number / DF)



단어의 중요도 ∝ TF ∝ IDF 그렇기 때문에 TF * IDF에도 비례한다

TF-IDF 값이 검색문의 문서 vector 가 된다. 그렇기 때문에 두 vector 간의 내적거리을 구하며 유사도를 측정 가능하다





#### Topic Model

차원 축소에는 두가지 방법이 있다

선형대수 이론 :  PCA ~ 														(고유값 분해)

​							SVD -~ Singluar Value Decomposition (특이값 분해)

SVD 는 차원축소 뿐 아니라 Topic Model 에도 쓰인다 'LSA' 

> LSA  = Latent Semantic Analysis 를 사용한다



##### Topic Model

LSA : SVD 원리를 사용한다

LDA : 결합확률 분포를 취급하며 문서와 단어 조합을 계산하는데, 이는 너무 어렵기 때문에 Sampling 기법을 사용한다. 이 중 'Gibbs' sampling 을 가장 많이 사용한다

LDA - 두개의 다항 분포를 추정하고, 해당 문서를 특정 topic 에 할당하는 것

![image-20200721162315662](markdown-images/image-20200721162315662.png)

이러한 flow 로 LDA 는 진행된다. 하지만, 실제 문제는 observed 된 document만 가지고 topic과 word를 추론한다.



### Text-to-Vector

#### 1. 통계적 기반, 빈도기반, 카운트 기반 => TFIDF, BOW(Bag of word)

#### Bow:

'I love you very much, you love me too'

vocab_list = [I : 0, love : 1, you : 2]

BoW 

> 1) [0, 1, 2 ..... 2, 1, x , y]

> 2) [(0,1), (1,2), (2,2).....]

Doc2Bow 실행시 2) 와 같이 적용이 된다

```python
import numpy as np
import re
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models.ldamodel import LdaModel as LDA
from sklearn.datasets import fetch_20newsgroups

newsData = fetch_20newsgroups(shuffle=True,
                             random_state=1,
                             remove=('headers', 'footers', 'quotes'))
# preprocessing 영문자가 아닌 문자를 regular expression 으로 제거
news1 = []
for doc in news:
    news1.append(re.sub("[^a-zA-Z]", " ", doc))
# stopwords(불용어)를 제거
# doc2bow 생성한다
vocab = corpora.Dictionary(news2)
dict(list(vocab.items())[:10])
news_bow = [vocab.doc2bow(s) for s in news2]
print(news_bow[0])

# 결과값은 아래와 같다
```

>{0: 'acts',
> 1: 'atrocities',
> 2: 'austria',
> 3: 'away',
> 4: 'biased',
> 5: 'blessing',
> 6: 'clearly',
> 7: 'commited',
> 8: 'daily',
> 9: 'degree'}

```python
model = LDA(news_bow, 
            num_topics = len(newsData.target_names), 
            id2word=vocab)
# LDA(corpus, num_topics=, id2word=(dict(int,str)))
```

토픽별로 중요 단어들이 나오게 된다



`vocab.token2id` 를 사용하면 vocab list 에서 속해있는 단어의 id 번호를 볼 수 있다



#### 2. Embedding 기반 (후술...)



### Document Summary

#### TextRank

각 문장의 TextRank 초기화...

TR(a) = TR(b) = TR(c) = TR(d) = 1/4 = 0.25

그 뒤 문서간 유사도를 측정 하고 해당 값을 통해 weight 를 제공한다

textRank 계산 - 반복 진행한다.

### Anaphora Resolution (조응어 해석)

John is a man. He walks. 에서 He 는 John을 재 표현한 것이다.

즉 He 는 John 에 의존 하며, 앞에 나온 단어에 의존 하는 것을 `전방조응`이라 하며 

I do not want to meet him. John was being mean to me. 와 같이 him 이 뒤에 나오는 문장 John을 의미한다면 `후방조응` 이라고 한다

이름을 구별하기 위해서는 문장 구조를 분해해야하고 (chunk), 이름의 성별을 구별하기 위해서 name corpus 를 사용한 학습을 진행한다. 



## Word Embedding

현재 NLP의 주류가 되는 원리는 단어기반이다. 이는 의미를 가지는 가장 작은 단위가 단어이기 때문이다. 

이러한 단어의 빈도수를 수치화 하여 자연어분석을 하는 방식이 지금까지 배운 TFIDF / BoW / Doc2BoW 같은 방식이다. 하지만 이런 빈도기반의 분석 방식은 단어 자체에 의미를 부여하지 못 하고 이로 인해 중요도 같은 판단에 있어 정확도가 낮아질 수 밖에 없다.

단어에게 의미를 부여하기 위해서는 학습 과정이 필요하며, 학습을 통해 단어를 수치화 (벡터화) 하는 방법을 통해 word embedding이 이루어진다.

![image-20200723102217467](markdown-images/image-20200723102217467.png)

단어간의 embedding 값을 가져와서 비교하는 것도 가능하고, CNN LSTM 을 병합하여 사용하는 것도 가능하다

단점 : 동음이의어에 대해서 같은 vector 가 주어지기 때문에 분석의 한계가 있다.

단어들의 관계, 의미적인 유사성을 갖도록 수치화한다 방법론적으로 학습을 통해 단어들을 수치 벡터로 변환한다



* 임베딩 벡터는 bias 값이 존재하지 않는다

### CBOW & Skip-gram

기계가 단어의 의미를 파악... 

#### CBOW(Continuous Bag of Words) 

주변의 단어를 기반으로 중간에 있는 단어를 예측하는 방식이다.

예시 문장 = 'I have played computer game' 

> 'I have ____________ computer game' 일 때 빈칸에 들어갈 수 있는 단어를 예측한다

각각의 center word(중심 단어), context word(주변 단어)를 one-hot으로 코딩되어있을 때, played를 center word 로 한다면 [0, 0, 1, 0 ,0]이 될 것이며, context word 는 have ([0, 1, 0, 0, 0]) 와 computer ([0,0,0,1,0]) 으로 표현 가능하다



#### Skip-gram

CBOW와 반대되는 개념으로 center word를 기반으로 context word를 예측하는 방식이다.

> computer 를 제공 했을 때 들어갈 수 있는 단어를 예측한다. 단순히 예측이 아닌 해당 단어들의 context 별로 묶어주는 vector 를 생산한다



##### 단점

1. word-embedding 의 특성을 따라 동음이의어에 대한 분석이 어렵다 (2020 현재로썬 해결하기 어렵다)
2. 출력층이 softmax (one=hot) 이기 때문에 계산량이 많다. 실무에서는 3~5 만개 정도의 vocab 이 계속 softmax 로 돌아간다. 
   * 해당 문제를 해결하기 위하여 Skip-gram Negative Sampling 이란 기법이 나오게 되었다. 
3. OOV 문제가 된다 새로운 단어에 대한 vector 가 없다보니 문제가 될 수 있다 

###### 보완방법

보완방법으로 FastText (OOV 처리), GloVe (Global Vectors for Word Representation) (TFIDF & Word2Vec 혼용), ELMo(Embeddings from Language Model) (동음이의어 처리)

## Hashing Trick

Corpus 단어를 사용하여 Vocabulary 를 만들어 one-hot 인코디을 진행하면 계산시간에 문제가 생긴다. (Expensive)

또한 OOV 문제를 해결하지 못 하는 단점이 존재한다

반면, Hash 기법을 사용할 경우 hash table 에 맞추어주기만 하면 되기 때문에 OOV 문제와 계산시간 문제를 해결 할 수 있다

다만 hash table 의 크기가 작아지면, 한개의 hash 에 여러개의 중첩 데이터가 발생 (collision) 할 수 있다

## 문서 유사도

### 자카드 유사도

두 개 문장의 교집합을 합집합으로 나눈 것

즉, 두 개의 문장이 공통으로 가지고 있는 단어들의 비율을 구해 문장간 유사도를 측정하는 방법이다

비율이기 때문에 0~1 까지의 값이 존재하며, 1에 가까울수록 공통 된 비율이 높다

### 코사인 유사도

수치화 된 단어 (벡터) 간 코사인 각도를 이용해 벡터의 유사도를 측정하는 방법 값이 1에 가까울수록 유사하다

문서의 길이가 다른 경우에도 상대적으로 공정한 유사도 비교가 가능하다

### 유클리디안 유사도

다차원 공간에 있는 두개의 점의 거리를 계산하는 방법으로 2차원에서는 피타고라스 공식을 생각하면 이해하기 편하다

값이 낮을수록 두 점의 거리가 가까운 것이기 때문에 문서 유사도 측정시 더 유사하다고 생각하면 된다

## Mutual Information

> "사상 x의 발생을 아는 데 따라 전해지는 정보량과 다른 사상 y가 발생한다는 조건 하에서 사상 x의 발생을 아는 데 따라서 전해지는 조건 있는 정보량과의 차."

PMI (A, B) = log( P(A,B) / P(A) × P(B) )

Doc2vec -> Dense ->

TFIDF -> Dense ->      concat -> dense -> sigmoid