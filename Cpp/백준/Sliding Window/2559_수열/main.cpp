#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2559. 수열
- 분류: Sliding Window
- 난이도: 실버 3
- 날짜: 2026.04.07
- 링크: https://www.acmicpc.net/problem/2559
*/
int N, K;
vector<int> temp;

int max_temp() {
    int sum = 0;

    for (int i = 0; i < K; i++) sum += temp[i];

    int result = sum;

    for (int i = K; i < N; i++) {
        sum += temp[i];
        sum -= temp[i-K];
        result = max(result, sum);
    }

    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> N >> K;
    temp.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> temp[i];
    }

    cout << max_temp();

    return 0;
}
