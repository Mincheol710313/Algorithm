#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2230. 수 고르기
- 분류: 투포인터
- 난이도: 골드 5
- 날짜: 2026.04.01
- 링크: https://www.acmicpc.net/problem/2230
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N, M;
    vector<int> arr;
    cin >> N >> M;
    arr.assign(N, 0);
    
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int left = 0, right = 0;
    int diff = 0;
    int result = -1;

    while (right < N) {
        if (diff == M) {
            result = M;
            break;
        } else if (diff > M) {
            if(result == -1) result = diff;
            else result = min(diff, result);
            left++;
            diff = arr[right] - arr[left];
        } else {
            right++;
            if (right < N) diff = arr[right] - arr[left];
        }
    }

    cout << result;

    return 0;
}
