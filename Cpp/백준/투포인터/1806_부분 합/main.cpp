#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1806. 부분 합
- 분류: 투포인터
- 난이도: 골드 4
- 날짜: 2026.04.01
- 링크: https://www.acmicpc.net/problem/1806
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N, S;
    vector<int> arr;
    cin >> N >> S;
    arr.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int left = 0, right = 0;
    int length = 0;
    int sum = arr[0];

    while (right < N) {
        if (sum >= S) {
            if (length == 0) length = right - left + 1;
            else length = min(length, (right - left + 1));
            sum -= arr[left++];
        } else if (sum < S) {
            right++;
            if (right < N) sum += arr[right];
        } 
    }

    cout << length;

    return 0;
}
