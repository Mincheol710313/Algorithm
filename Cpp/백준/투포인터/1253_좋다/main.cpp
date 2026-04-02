#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1253. 좋다
- 분류: 투포인터
- 난이도: 골드 4
- 날짜: 2026.04.02
- 링크: https://www.acmicpc.net/problem/1253
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    vector<int> arr;
    cin >> N;
    arr.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int count = 0;
    for (int i = 0; i < N; i++) {
        int target = arr[i];

        int left = 0, right = N-1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            
            if (sum == target) {
                if(left != i && right != i) {
                    count++;
                    break;
                } else if (left == i) {
                    left++;
                } else {
                    right--;
                }   
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    cout << count;

    return 0;
}
