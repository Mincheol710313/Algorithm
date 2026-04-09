#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1463. 1로 만들기
- 분류: 동적프로그래밍
- 난이도: 실버 3
- 날짜: 2026.04.09
- 링크: https://www.acmicpc.net/problem/1463
*/
vector<int> dp(1000001, -1);

void bottom_up_sol() {
    dp[1] = 0;

    for(int i = 2; i <= 1000000; i++) {
        dp[i] = dp[i-1] + 1;
        if (i % 2 == 0) dp[i] = min(dp[i], dp[i/2] + 1);
        if (i % 3 == 0) dp[i] = min(dp[i], dp[i/3] + 1);
    }
}

int top_down_sol(int n) {
    if(n == 1) return 0;
    if(dp[n] != -1) return dp[n];
    
    dp[n] = top_down_sol(n-1) + 1;
    if(n % 2 == 0) dp[n] = min(dp[n], top_down_sol(n/2) + 1);
    if(n % 3 == 0) dp[n] = min(dp[n], top_down_sol(n/3) + 1);

    return dp[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;

    // bottom_up_sol();

    cout << top_down_sol(N);
    return 0;
}
