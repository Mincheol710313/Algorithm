# 시간 초과 문제 생각해보기
import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

new_list = [0] * N
for i in range(N):
   num = 0
   relevant_list = []
   for j in range(N):
       if num_list[i] > num_list[j]:
           if (num_list[i], num_list[j]) not in relevant_list:
               relevant = (num_list[i], num_list[j])
               relevant_list.append(relevant)
               num += 1

   new_list[i] = num


for i in range(N):
    print(new_list[i], end=' ')