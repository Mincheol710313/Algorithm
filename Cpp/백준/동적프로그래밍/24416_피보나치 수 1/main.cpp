#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 24416. 피보나치 수 1
- 분류: 동적프로그래밍
- 난이도: 브론즈 1
- 날짜: 2026.04.08
- 링크: https://www.acmicpc.net/problem/24416
*/
int N;

int fib_count = 0;
int fib(int n) {
    if(n == 1 || n == 2) {
        fib_count++;
        return 1;
    }
    else return (fib(n-1) + fib(n-2));
}

vector<int> f;
int fibonacci(int n) {
    int count = 0;
    if (n == 1 || n == 2) return f[1];

    for (int i = 3; i < n+1; i++) {
        f[i] = f[i-1] + f[i-2];
        count++;
    }

    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> N;
    f.assign(41, 0);
    f[1] = 1; f[2] = 1;
    fib(N);
    
    cout << fib_count << " " << fibonacci(N);

    return 0;
}
