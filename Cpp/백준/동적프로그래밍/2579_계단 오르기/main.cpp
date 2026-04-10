#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2579. 계단 오르기
- 분류: 동적프로그래밍
- 난이도: 실버 3
- 날짜: 2026.04.10
- 링크: https://www.acmicpc.net/problem/2579
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;

    vector<int> step_arr(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        cin >> step_arr[i];
    }

    vector<int> dp(N + 1, 0);
    dp[1] = step_arr[1];
    dp[2] = step_arr[1] + step_arr[2];

    for (int i = 3; i <= N; i++) {
        dp[i] = max(dp[i-2] + step_arr[i], dp[i-3] + step_arr[i-1] + step_arr[i]);
    }

    cout << dp[N];

    return 0;
}
