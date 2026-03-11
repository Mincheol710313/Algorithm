#include <iostream>
#include <string>
#include <deque>

using namespace std;

/*
- [백준] 10866. 덱
- 분류: 자료구조
- 난이도: 실버 4
- 날짜: 2026.03.11
- 링크: https://www.acmicpc.net/problem/10866
*/

int main() {
// TODO: 풀이 작성
    int cmd_num;
    cin >> cmd_num; // 명령어 개수 입력

    deque<int> d; // deq으로 사용할 queue 정의

    for (int i = 0; i < cmd_num; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push_front") {
            int num;
            cin >> num;
            d.push_front(num);
        } else if (cmd == "push_back") {
            int num;
            cin >> num;
            d.push_back(num);
        } else if (cmd == "pop_front") {
            if (d.empty()) {
                cout << -1 << endl;
            } else {
                cout << d.front() << endl;
                d.pop_front();
            }
        } else if (cmd == "pop_back") {
            if (d.empty()) {
                cout << -1 << endl;
            } else {
                cout << d.back() << endl;
                d.pop_back();
            }
        } else if (cmd == "size") {
            cout << d.size() << endl;  
        } else if (cmd == "empty") {
            cout << d.empty() << endl;
        } else if (cmd == "front") {
            cout << (d.size() == 0 ? -1 : d.front()) << endl;
        } else if (cmd == "back") {
            cout << (d.size() == 0 ? -1 : d.back()) << endl;
        }
    }


    return 0;
}
