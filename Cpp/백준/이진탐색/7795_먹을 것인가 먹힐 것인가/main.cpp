#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 7795. 먹을 것인가 먹힐 것인가
- 분류: 이진탐색
- 난이도: 실버 3
- 날짜: 2026.03.14
- 링크: https://www.acmicpc.net/problem/7795
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int test_num;
    cin >> test_num;

    for (int i = 0; i < test_num; i++) {
        int hunter_num, prey_num;
        cin >> hunter_num >> prey_num;

        vector<int> hunters, preys;
        for (int j = 0; j < hunter_num; j++) {
            int hunter;
            cin >> hunter;
            hunters.push_back(hunter);
        }

        for (int j = 0; j < prey_num; j++) {
            int prey;
            cin >> prey;
            preys.push_back(prey);
        }

        sort(preys.begin(), preys.end());

        int total = 0;
        for (int hunter : hunters) {
            total += lower_bound(preys.begin(), preys.end(), hunter) - preys.begin();
        }

        cout << total << "\n";
    }
    
    return 0;
}
