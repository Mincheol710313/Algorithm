"""
MenOfPassion 알고리즘 분석

MenOfPassion(A[], n){
    i = [n / 2]
    return A[i] # 코드 1
}

Parameter : A[](list), n(int)
Output : A[i] -> 단순 list 접근
따라서 코드 1 의 수행 횟수는 n과 상관없이 "1"번만 일어난다! 따라서 빅오표기법에 의해 O(1)이다!
결국 알고리즘 수업-알고리즘의 수행시간은 단순히 MenOfPassion의 알고리즘을 분석하는 것이다.

빅오표기법
"""
import sys

n = int(sys.stdin.readline().rstrip())
print(1)
print(0)
