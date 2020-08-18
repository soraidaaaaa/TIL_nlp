# 챗봇 만들기

## Sequence to Sequence Model (Seq2Seq)

Encoder 와 Decoder 두개의 RNN모델로 이루어져있으며, 성능을 위해 LSTM 혹은 GRU 모델이 사용된다. 데이터의 구성은 Input 두개와 Target 한개로 이루어져있다. Input 의 경우 encoder 와 decoder에 각각 하나씩 embeding layer 이후에 들어가며, Target은 many-to-many 모델로 decoder의 target으로 자리하게 된다. 

Encoder는 many-to-one 모형을 띄며 결과값으로 short-term state (h), long-term state(c)를 출력하는데 이 값을 가지고 decoder 의 input 과 연계하여 decoder 의 target 값을 one-hot 으로 출력한다. one-hot 으로 출력하기 때문에 softmax를 사용하며, 마지막엔 END 를 출력한다. 

### Prediction

학습 단계에서는 decoder 에서도 나올 값을 알고 있기 때문에 문제가 없다. 그렇기 때문에 학습할 때는 Decoder의 input 을 한번에 recurrent 할 수 있다. (Teacher Forcing 개념) 

하지만, chatbot 의 경우 encoder input 이 들어온 뒤 decoder input의 첫번째만 알지 그 이후는 알 수가 없다. 때문에 for 문을 통해 time step 을 하나하나 직접 짜준다. 



## Seq2Seq-Attention Model

seq2seq2 모델의 경우 고정된 크기의 벡터에 정보를 압축하다보니 정보 손실이 발생한다. 이를 보정하기 위해 attention 모델이 개발되었다. Attention의 기본 아이디어는 decoder 의 출력 time step 마다 인코더에서 천체 입력 문장을 다시 한 번 참고 하여 진행하는 것이다. 단순히 연관성 있는 단어를 찾는 것이 아닌 관련 있는 단어에 집중을 하는 것이다.

attention score를 구해서 encoder 의 출력값과 다시 곱하여 attention value 를 구한 뒤 decoder의 값과 concatenate 해주어서 최종 output value를 구한다.

## Transformer Model (Self-Attention)

Attention 모델에서 RNN(LSTM)을 제거한 모델로, 인코더와 디코더 모두 attention 모델로 이루어져 있다. 인코더와 디코더 모두 여러 단계의 층으로 구성되어있으며, multi-haed attention, feedfoward network 등 이후에 add&normalization 과정이 진행된다.

Attenton 모델과는 다르게 encoder와 decoder 모두 e 값을 반환하며, 각각 W, K, V 값으로 불린다. Attention 모델의 경우 K와 V의 값이 같지만, transformer에서는 각각 다른 weight 때문에 다른 값이 될 수 있다.

### FastText

word2vec은 oov문제가 존재한다. 이를 보완하기 위해 FastText 개념이 사용되었다. 기본 toekn 사전을 구축한 뒤 n-gram character 방식으로 sub-word 개념을 사용한다. hash-table 을 vocab-size 보다 크게 생성을 해서 미리 확보해둔다. 

word2vec 형식의 경우 단어를 tokenizing 한 후에 embedding 을 진행하여 단어를 한개의 vector로 생산한다. 반면, hash-table 에는 collision 이 발생할 수 있지만 DB 에서 overflow table을 사용하여 문제를 해결한다. 하지만 overflow page 가 늘어나면 검색 속도가 떨어지고, 너무 수가 많아지면 (임계치를 초과) hash-table 을 늘려서 DB 를 재구성 한다 'reorganization'.  기존의 단어들의 위치가 변경된다. 

### WordPiece, Byte pair encoding, Sentence Piece

빈도가 높은 문자열들은 하나의 "unit" 으로 사전에 등록하여 사용한다. 

> 나는 학교에 간다

라는 문장을 '학교' '나' ' 는'  '간다' 로 나누어 빈도를 관찰한다 