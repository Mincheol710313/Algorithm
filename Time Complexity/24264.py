"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j] # 코드1
    return sum;
}
Input : A[], n
Output : A[]에 있는 요소 중 0 ~ n 까지의 요소 0 ~ n까지의 요소와 곱한 값을 더한 결과
"""
n = int(input())
print(n*n)
print(2)