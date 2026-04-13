#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2156. 포도주 시식
- 분류: 동적프로그래밍
- 난이도: 실버 1
- 날짜: 2026.04.13
- 링크: https://www.acmicpc.net/problem/2156
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;
    vector<int> grape(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> grape[i];
    }

    vector<int> dp(N,0);
    dp[0] = grape[0];
    dp[1] = grape[0] + grape[1];
    dp[2] = max(grape[0] + grape[1], max(grape[0] + grape[2], grape[1] + grape[2]));

    for (int i = 3; i < N; i++) {
        dp[i] = max(dp[i-1], max(dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i]));
    }

    cout << dp[N-1];

    return 0;
}
