# Logistic Regression

## 개념

linear regression에서 y가 종속변수일 때는 Ordinary Least Square가 유효하며, y도 독립변수 일 때는 Total Least Square 방식이 더 유효하다. 

regession 중에서 binary classification이 가능한 logistic ression 이다

일반 linear regression 처럼 mean square error 를 사용 가능하지만, cross entorpy를 사용하는 것이 편하다

Cross Entropy 의 개념은 information gain 에서 출발한다 

> 확률이 낮은 사건이 발생할 때 information gain이 상승하고 반대의 경우 information gain이 하락한다. 
>
> 독립적인 두 사건의 발생 확률은 서로 곱해져야하지만, 정보량은 곱해지는 것이 어색하기 때문에 log 처리하여 더하기로 한다.

## CE (cross entropy) 와 Loss Function의 관계

loss function으로 cross entropy를 사용한다

### BCE 와 CCE

Binary cross entropy 와 Categorical cross entropy는 상황에 맞게 사용하여야한다.

Binary cross entropy의 경우 sigmoid 값을 출력해주며

Categorical cross entropy의 경우 softmax 값을 출력해준다.

하지만 multi label classification의 경우 binary cross entropy 가 사용될 수도 있으니 유의하자!!!

### regularization

학습을 통해 loss 를 줄이는 weights 를 찾아야한다.

하지만 특정 weights 가 과도하게 커진다면 feature의 값에 영향을 많이 받게 되며 overfitting의 위험이 발생ㅎ나다. 이 것을 방지하기 위해 loss 함수에 penalty항을 추가한다. 

L1 / L2 방식의 regularization이 존재하며,  차이점은 L1 방식의 경우 일부 weights를 0으로 설정하며, L2 의 경우 모든 weights의 크기를 변경하지 않음

