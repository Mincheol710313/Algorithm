#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1912. 연속합
- 분류: 동적프로그래밍
- 난이도: 실버2
- 날짜: 2026.04.13
- 링크: https://www.acmicpc.net/problem/1912
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;
    vector<int> arr(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector<int> dp(N, 0);
    dp[0] = arr[0];
    for (int i = 1; i < N; i++) {
        dp[i] = max(arr[i], dp[i-1] + arr[i]);
    }

    int result = dp[0];
    for (int i = 1; i < N; i++) {
        result = max(result, dp[i]);
    }

    cout << result;

    return 0;
}
