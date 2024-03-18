"""
음료수 얼려 먹기
N x M 크기의 얼음 틀이 있을 때, 구멍이 뚫려 있는 부분 0, 칸막이가 존재하는 부분 1
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
"얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램"
--> 연결 요소 찾기(Connected Component Find)
DFS 혹은 BFS로 해결 가능할 수 있다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())