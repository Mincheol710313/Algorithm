#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 9184. 신나는 함수 실행
- 분류: 동적프로그래밍
- 난이도: 실버 2
- 날짜: 2026.04.09
- 링크: https://www.acmicpc.net/problem/9184
*/
int a, b, c;
vector<vector<vector<int>>> dp;

int w(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) return 1;
    if (a > 20 || b > 20 || c > 20) return w(20,20,20);

    if(dp[a][b][c] != -1) return dp[a][b][c];

    if(a < b && b < c) return dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);

    return dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    dp.assign(21, vector<vector<int>>(21, vector<int>(21, -1)));
    while(true) {
        cin >> a >> b >> c;

        if (a == -1 && b == -1 && c == -1) break;
        else {
            cout << "w(" << a << ", "<< b << ", " << c << ") = " << w(a, b, c) << "\n";
        }
    }

    return 0;
}
