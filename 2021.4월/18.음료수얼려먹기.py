# 음료수 얼려먹기
# 2021.04.17. 
'''
N * M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
얼음 틀 모양이 주어졌을 때, 생성되는 아이스크림의 개수를 구하는 프로그램을 작성하라.

EX 
00110
00011
11111
00000

출력 : 3

'''



n, m = map(int, input().split())
# N, M을 공백으로 구분하여 입력받기

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

