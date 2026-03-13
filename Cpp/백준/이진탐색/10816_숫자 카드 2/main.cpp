#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

/*
- [백준] 10816. 숫자 카드 2
- 분류: 이진탐색
- 난이도: 실버 4
- 날짜: 2026.03.13
- 링크: https://www.acmicpc.net/problem/10816
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_count;
    cin >> num_count;

    unordered_map<int,int> number_counts;

    for (int i = 0; i < num_count; i++) {
        int num;
        cin >> num;
        if (number_counts.find(num) == number_counts.end()) number_counts[num] = 1;
        else number_counts[num] += 1;
    }

    int check_count;
    cin >> check_count;

    for (int i = 0; i < check_count; i++) {
        int check_num;
        cin >> check_num;
        if (number_counts.find(check_num) == number_counts.end()) cout << 0 << " ";
        else cout << number_counts[check_num] << " ";
    }

    return 0;
}