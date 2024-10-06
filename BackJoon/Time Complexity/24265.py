"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
Input : 이전 문제들과 동일
Output : 이전 문제와 다르게 0 ~ n-1과 해당 값보다 큰 인덱스를 가지고 있는 애들과의 곱의 합 결과
따라서 빅오표시범으로 O(n^2)로 이전과 동일하지만 코드1 실행횟수는 n*(n+1)/2 번이다.
"""
n = int(input())
print(int(n*(n-1)/2))
print(2)