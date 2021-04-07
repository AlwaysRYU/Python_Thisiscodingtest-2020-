# 0. 주석 달기
# 주석다는 방법 : ''' """
# 또는 ctl + /

# def sum(a,b) :
#     #더하기 함수
#     print(a+b)

# 1. split
# split( seq = '', max split = -1) 문자열을 나누는 함수
# seq : 문자열을 구분하는거
# maxsplit : 분리할 문자개수를 지정할 때 사용됨

# examplemal = '우리는 모두 괜찮습니다.'
# print(examplemal)
# examplemal.split(' ')
# print(examplemal)


# 2. for 문
# for 변수 in 리스트 :
# ...

exlist = ['one', 'two', 'three']
for i in exlist:
    print(i)


# 3. range
# 숫자 리스트를 자동으로 만들어주는 range 함수

add = 0
for i in range(1,11):
    add = add + i
print(add)

# 4. iterator 이터레이터
# 파이썬에서 반복자는 여러개의 요소를 가지는 컨테이너(리스트, 튜플, 셋, 사전 문자열)에서 각 요소를 하나씩 꺼내 수행하는 간편한 방법을 제공하는 객체


# 5. map
# map(f, iterable)은 함수 f와 반복가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려주는 함수이다. 
# map(적용시킬 함수, 적용시킬 요소)
# map(함수, 리스트)

#리스트 데이터를 두배를 곱하는 함수
def two_times(alist):
    result = []
    for number in alist:
        result.append(number*2)
    return result

result1 = two_times([1,2,3,4])
print(result1)

def two_times2(nn):
    return nn*2

list2 = map(two_times2, [1,2,3,4])
print(list(list2))



# 6. lambda
'''
함수의 재사용의 목적이 없다면 lambda로 바꿔도 된다.
함수를 딱 한줄만으로 만들게 해주는 친구.
lambda 인자 : 표현식
'''
#xy의 합을 구하는 함수
def hap(x,y):
    return x + y
print(hap(10,20))
#를 lambda로는 이렇게 표현 가능
(lambda x,y : x + y)(10,20)


#map과의 차이
#이건 x값을 제곱하라는 함수
list(map(lambda x: x**2, range(5)))


print('파이썬의 언더스코어')
#7. 파이썬의 언더스코어 _
'''
파이썬의 언더스코어 _
값을 무시하고 싶을 때 / 변수에 특별한 의미를 부여할대, 제화 함수로 사용할 때
1. 마지막으로 실행했던 결과 값이 _ 라는 변수에 저장
2. 값을 무시하고 싶은 경우
'''
x, _, y = (1, 2, 3,)
print(x, y)
x, *_, y = (1,2,3,4,5,6,7,8)
print(x,y)

for _ in range(3):
    print("악")
# 따로 i를 사용하지 않아도 반복문 이가능하다.