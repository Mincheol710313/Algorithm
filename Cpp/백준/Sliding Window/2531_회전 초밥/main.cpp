#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2531. 회전 초밥
- 분류: Sliding Window
- 난이도: 실버 1
- 날짜: 2026.04.07
- 링크: https://www.acmicpc.net/problem/2531
*/
int N, D, K, C;
vector<int> susi_arr;
vector<int> susi_count;

int max_distinct() {
    int distinct = 0;

    for (int i = 0; i < K; i++) {
        if (susi_count[susi_arr[i]] == 0) {
            distinct++;
        }
        susi_count[susi_arr[i]]++;
    }

    int result = distinct + (susi_count[C] == 0 ? 1 : 0);

    for (int i = K; i < N+K-1; i++) {
        if(susi_count[susi_arr[i]] == 0) distinct++;
        susi_count[susi_arr[i]]++;

        susi_count[susi_arr[i-K]]--;
        if(susi_count[susi_arr[i-K]] == 0) distinct--;

        result = max(result, distinct + (susi_count[C] == 0 ? 1 : 0));
    }

    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> N >> D >> K >> C;
    susi_arr.assign(2*N, 0);
    susi_count.assign(D+1, 0);

    for (int i = 0; i < N; i++) {
        cin >> susi_arr[i];
        susi_arr[N+i] = susi_arr[i];
    }

    cout << max_distinct();

    return 0;
}
