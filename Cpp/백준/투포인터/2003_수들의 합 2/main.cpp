#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2003. 수들의 합 2
- 분류: 투포인터
- 난이도: 실버 4
- 날짜: 2026.03.31
- 링크: https://www.acmicpc.net/problem/2003
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N, M;
    vector<int> array;
    cin >> N >> M;
    array.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }

    int left = 0, right = 0;
    long long sum = array[0];
    int count = 0;

    while (right < N) {
        if (sum == M) {
            count++;
            sum -= array[left++];
        } else if (sum < M) {
            right++;
            if (right < N) sum += array[right];
        } else {
            sum -= array[left++];
        }
    }

    cout << count;

    return 0;
}
