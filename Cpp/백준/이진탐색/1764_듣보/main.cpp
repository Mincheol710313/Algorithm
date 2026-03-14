#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 1764. 듣보
- 분류: 이진탐색
- 난이도: 실버 4
- 날짜: 2026.03.14
- 링크: https://www.acmicpc.net/problem/1764
*/

bool human_binary_search(vector<string>& v, string target) {
    int start = 0, end = v.size() - 1;
    while(start <= end) {
        int mid = (start + end) / 2;

        if(v[mid] == target) return true;
        else if(v[mid] < target) start = mid + 1;
        else end = mid - 1;
    }

    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int not_listen_num, not_see_num;
    cin >> not_listen_num >> not_see_num;

    vector<string> not_listens, not_sees;
    for(int i = 0; i < not_listen_num; i++) {
        string not_listen;
        cin >> not_listen;
        not_listens.push_back(not_listen);
    }

    for(int i = 0; i < not_see_num; i++) {
        string not_see;
        cin >> not_see;
        not_sees.push_back(not_see);
    }

    sort(not_listens.begin(), not_listens.end());
    sort(not_sees.begin(), not_sees.end());

    vector<string> not_listen_see;
    if(not_listen_num <= not_see_num) {
        for(int i = 0; i < not_listen_num; i++) {
            if(human_binary_search(not_sees, not_listens[i])) not_listen_see.push_back(not_listens[i]);
        }
    } else {
        for(int i = 0; i < not_see_num; i++) {
            if(human_binary_search(not_listens, not_sees[i])) not_listen_see.push_back(not_sees[i]);
        }
    }

    cout << not_listen_see.size() << "\n";
    for(string name : not_listen_see) cout << name << "\n";

    return 0;
}
