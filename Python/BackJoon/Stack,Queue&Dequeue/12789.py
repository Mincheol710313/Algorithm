import sys
N = int(input())  # 학생들의 수
num_list = sys.stdin.readline().rstrip()  # 학생들의 번호표 순서
num_list = list(map(int, num_list.split()))
stack = []
