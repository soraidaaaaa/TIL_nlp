#  Support Vector Machine

## 개념

SVM 은 binary classification 을 기본으로 하며 multi-class classification일 경우 한 개의 class 와 나머지의 이진분류를 어려번 진행한다.

SVM 은 이진분류를 통해 margin 의 크기를 줄여나가는 것이 목표이다

물론 예외값이 존재하지만 이런 값은 계산 시 slack 변수를 추가하여 허용해준다.....

## Kernel Trick

비선형 SVM 문제가 생길 수 있다 (직선보다 곡선이 분류를 하는데 타당한 경우)

이럴 경우 원래의 데이터를 변환시켜 (차원의 수를 늘려)선형 분리가 가능하게 만든 뒤 분류한다

무한하게 차원을 늘린다면 무조건 선형 분리가 가능하지만, 차원이 높아질수록 차원의 저주에 의해 계산량이 상승하기 때문에,적절히 사용하여야 한다. 