#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1003. 피보나치 함수
- 분류: 동적프로그래밍
- 난이도: 실버 3
- 날짜: 2026.04.08
- 링크: https://www.acmicpc.net/problem/1003
*/
int T, N;
vector<int> zero_count;
vector<int> one_count;

void fib() {
    zero_count[0] = 1; zero_count[1] = 0;
    one_count[0] = 0; one_count[1] = 1;

    for (int i = 2; i < 41; i++) {
        zero_count[i] = zero_count[i-1] + zero_count[i-2];
        one_count[i] = one_count[i-1] + one_count[i-2]; 
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    zero_count.assign(41, 0);
    one_count.assign(41, 0);
    fib();
// TODO: 풀이 작성
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        cout << zero_count[N] << " " << one_count[N] << "\n";
    }

    return 0;
}
