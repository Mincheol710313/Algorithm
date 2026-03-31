#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1940. 주몽
- 분류: 투포인터
- 난이도: 실버 4
- 날짜: 2026.03.31
- 링크: https://www.acmicpc.net/problem/1940
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N, M;
    cin >> N;
    cin >> M;
    vector<int> arr;
    arr.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int left = 0, right = N-1;
    int count = 0;

    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == M) { 
            count++;
            left++;
            right--;
        } else if (sum < M) {
            left++;
        } else {
            right--;
        }
    }

    cout << count;

    return 0;
}