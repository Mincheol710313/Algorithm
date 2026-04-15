#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 11722. 가장 긴 감소하는 부분 수열
- 분류: 동적프로그래밍
- 난이도: 실버 2
- 날짜: 2026.04.15
- 링크: https://www.acmicpc.net/problem/11722
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    cin >> N;

    vector<int> arr(N,0);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector<int> dp(N, 0);
    for (int i = 0; i < N; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if(arr[i] < arr[j]) dp[i] = max(dp[i], dp[j] + 1);
        }
    }

    int result = dp[0];
    for (int i = 1; i < N; i++) {
        result = max(result, dp[i]);
    }

    cout << result;
    return 0;
}