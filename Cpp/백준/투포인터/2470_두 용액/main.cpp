#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2470. 두 용액
- 분류: 투포인터
- 난이도: 골드 5
- 날짜: 2026.04.02
- 링크: https://www.acmicpc.net/problem/2470
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    vector<int> liquid;
    cin >> N;
    liquid.assign(N,0);

    for (int i = 0; i < N; i++) {
        cin >> liquid[i];
    }

    sort(liquid.begin(), liquid.end());

    int left = 0, right = N-1;
    int result = liquid[right] + liquid[left];
    pair<int, int> ans = {liquid[left], liquid[right]};
    while (left < right) {
        int sum = liquid[right] + liquid[left];

        if (sum == 0) {
            ans = {liquid[left], liquid[right]};
            break;
        } else if (sum > 0) {
            if (abs(result) > abs(sum)) {
                result = sum;
                ans = {liquid[left], liquid[right]};
            }
            right--;
        } else {
            if (abs(result) > abs(sum)) {
                result = sum;
                ans = {liquid[left], liquid[right]};
            }
            left++;
        }
    }

    cout << ans.first << " " << ans.second;

    return 0;
}
