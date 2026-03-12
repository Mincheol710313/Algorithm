#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

/*
- [백준] 1920. 수 찾기
- 분류: 자료구조
- 난이도: 실버 4
- 날짜: 2026.03.12
- 링크: https://www.acmicpc.net/problem/1920
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    std::unordered_map<int, int> number_map;

    int N;
    cin >> N;

    for(int i = 0; i < N; i++){
        int input_num;
        cin >> input_num;

        number_map[input_num] = 1;
    }

    int M;
    cin >> M;
    for(int i = 0; i < M; i++) {
        int find_num;
        cin >> find_num;

       if(number_map.find(find_num) != number_map.end()) {
            cout << 1 << "\n";
       } else cout << 0 << "\n";
    }

return 0;
}
