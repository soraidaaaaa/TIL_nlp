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

