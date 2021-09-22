# 1일 1코딩테스트 프로젝트

## 개요 
* 사용언어 및 IDE :   
 Python3, Java(2021.07.17.추가), SQL(2021.09.07.추가)     
 VScode
* 기간 :   
 2021.03.14 ~ 현재    
 
 
## 내용   
1. 하루에 한 번 코딩 문제를 풀기
2. 혼자 해결하지 못 한 경우, 리스트를 만들어서 정리해놓기

### 폴더
|폴더 이름| 내용||
|:--:|:--:|:---:|
|20xx.x월|월별 파일 폴더||
|Python 학습| python의 라이브러리/자료구조 학습 정리||
|Java 학습| 코딩에 필요한 기초 자료구조/라이브러리 등 Java학습정리||
|도서내용정리|<이것이 취업을 위한 코딩테스트다> 를 읽고 도서 내용 정리||
|나머지정리폴더|기타 메모용, 테스트용 파일||

##### 파일명
* 언어가 java : J01, J02, J03 ..
* 언어가 Python : P01, P02, P03 ..
* 언어가 SQL : SQL01, SQL02, SQL03 ..

## 최종목표   
* 코딩테스트 전형을 반가워 할 수 있는 정도의 능력을 갖기
* 프로그래머스 Level 3 정도의 문제를 막힘없이 풀 수 있는 실력 구비

## 소감, 여담
* 2021.07.17.   
    2021월 3월 14일 부터 파이썬으로 매일매일 코딩문제를 푸는 것을 목표로 했습니다.    
    하지만 이번에 SSAFY 6기 Java 전공반으로 입과하면서, Java와 관련 기술 들을 배웁니다.   
    기존의 폴더에 .py 와 .java를 같이 사용할 경우 실행에 오류가 있어 java는 따로 작성하고 MD파일로 옮겨서 작성하도록 합니다.
* 2021.09.07.  
    오랜만에 SQL을 하니 재밌습니다.   
    SQL문제도 지속적으로 풀어야겠습니다.   
***

## 문제를 풀면서 느낀 팁 들
* 입력의 사이즈가 작다고 느낄 경우, 모든 케이스를 검사해서 답을 구하는 것이 맞을 때가 있다.
>ex 202107의 자물쇠와열쇠 문제

* 그래프 문제의 경우, 모든 도로의 거리나 간선의 거리가 동일하다는 조건은 너비우선탐색을 이용하는 것을 생각해보자.

*** 

## 코딩테스트 관련 용어
* 문제 종류        
    + 결정문제 : 예/아니요로 끝나는 문제        
    + 최적화문제 : 최적인 답을 찾는 문제        
    + 시뮬레이션 문제(구현 문제) : 문제에서 제시한 구체적인 처리과정을 프로그램 상에서 구현하는 문제 

* 파라메트릭(Parametric) 서치?   
    최적화문제를 결정문제로 바꾸어 해결하는 기법    
    범위 내에서 조건을 만족하는 가장 큰 값을 찾아라 -> 이진탐색 활용   
    코딩테스트/대회 에서는 보통 이진탐색을 사용한다.   
    > 예시 : 2021 6월/01부품찾기.py   
    > 적절한 답을 찾을 때 까지 조정한다.   
    > 시작은 중간자로 하는 것이 좋다.    
    > 만족하는가? (Y/N) => 조정 후 반복

* 브루트 포스       
    brute force -> 무식한 힘이다.       
    암호학에서 조합가능한 모든 문자열을 대입해보는 기법을 말한다.       
    즉, 알고리즘에서는 완전탐색 알고리즘이다. 전수조사라고도 할 수 있겠다..
    주로 주어진 문제를 선형구조로 구조화하여 풀도록 하자.

* 문제를 푸는 시간
    5초 : 비교적 넉넉한 시간이다. 전체를 확인해도 되는 건지 생각해보자.
    1000ms = 1 초
    
### 효율적인 코드를 작성하는 방법   
* 다이나믹프로그래밍의 경우 / 재귀의 경우   
    + 리스트를 사용한다. (메모지에이션 기법 ) 리스트에다가 값을 정하는 경우


## 참고 서적 및 사이트
* ### 도서  
    + 이것이 취업을 위한 코딩테스트다 with 파이썬(한빛미디어)
    + Do it! 자료구조와 함께 배우는 알고리즘 입문 (java편)
* ### 웹 사이트 :    
    + 프로그래머스의 코딩테스트 문제 (https://programmers.co.kr/)   
    + 삼성 SW Expert 아카데미 (https://swexpertacademy.com/main/main.do)      
    + 백준(https://www.acmicpc.net/)
    + 백준의 SW역량테스트 기출 문제 + code.plus 문제집 (https://www.acmicpc.net/workbook/view/1152)
    + 정보 올림피아드 (http://jungol.co.kr/)
 
 ***
 
