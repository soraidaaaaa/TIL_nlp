# Git

> Git 은 분산형 버전 관리 시스템이다...

## 0. Git 기초설정

* 윈도우 환경에서는 'git for windows 로 검색하여 `git bash` 를 설치한다.   [다운로드 링크](https://gitforwindows.org/)

* 최초에 컴퓨터에서 git을 사용하는 경우 아래의 설정을 진행한다. 

  ```bash
  $ git config --global user.email 이메일주소
  $ git config --global user.name 유저네임
  # 확인
  $ git config --global -l
  ```

  * 이메일 주소를 설정할 때, github 에 가입된 이메일로 설정 해야 커밋 이력이 github에 기록된다... (주의)

## 1. Git을 통한 버전관리 기본 흐름

### 1.1 Git 저장소 초기화

> 특정 폴더를 git 저장소로 활용하기 위해서 최초로 입력하는 명령어

```bash 
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/TIL/.git/

student@M1702 MINGW64 ~/Desktop/TIL (master)
```

* .git 폴더가 숨긴 폴더로 생성되며, git bash 에서는 `(master)` 라고 표기된다.
* 반드시 git으로 활용되고 있는 폴더 아래에서 저장소를 선언하지 말자...

### 1.2 add



