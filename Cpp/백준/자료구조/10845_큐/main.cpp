#include <iostream>
#include <string>
#include <queue>

using namespace std;

/*
- [백준] 10845. 큐
- 분류: 자료구조
- 난이도: 실버 4
- 날짜: 2026.03.11
- 링크: https://www.acmicpc.net/problem/10845
*/

int main() {
    // TODO: 풀이 작성
    int cmd_num; // 명령의 수
    cin >> cmd_num;

    queue<int> q; // 큐 선언

    for (int i = 0; i < cmd_num; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int num;
            cin >> num; // 추가 값 읽기
            q.push(num);
        } else if (cmd == "pop") {
            if(q.size() == 0) cout << -1 << endl;
            else {
                cout << q.front() << endl;
                q.pop();
            }
        } else if (cmd == "size") {
            cout << q.size() << endl;
        } else if (cmd == "empty") {
            cout << q.empty() << endl;
        } else if (cmd == "front") {
            if(q.size() == 0) cout << -1 << endl;
            else cout << q.front() << endl;
        } else if (cmd == "back") {
            if(q.size() == 0) cout << -1 << endl;
            else cout << q.back() << endl;
        }
    }

    return 0;
}
