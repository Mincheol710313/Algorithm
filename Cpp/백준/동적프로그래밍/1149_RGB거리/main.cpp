#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1149. RGB거리
- 분류: 동적프로그래밍
- 난이도: 실버 1
- 날짜: 2026.04.10
- 링크: https://www.acmicpc.net/problem/1149
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;
    vector<vector<int>> home_arr(N, vector<int>(3, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> home_arr[i][j];
        }
    }

    vector<vector<int>> dp(N, vector<int>(3, 0));
    for (int i = 0; i < 3; i++) {
        dp[0][i] = home_arr[0][i];
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home_arr[i][0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home_arr[i][1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + home_arr[i][2];
    }

   cout << min(dp[N-1][0], min(dp[N-1][1], dp[N-1][2]));

    return 0;
}
