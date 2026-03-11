#include <iostream>
#include <string>
#include <stack>

using namespace std;

/*
- [백준] 10828. 스택
- 분류: 자료구조
- 난이도: 실버 4
- 날짜: 2026.03.11
- 링크: https://www.acmicpc.net/problem/10828
*/

int main() {
// TODO: 풀이 작성
    int cmd_num;
    cin >> cmd_num; // 명령의 입력받아 저장

    stack<int> s; // stack 생성

    for (int i = 0; i < cmd_num; i++) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int num;
            cin >> num;

            s.push(num);
        } else if (cmd == "pop") {
            if(s.size() == 0) cout << -1 << endl;
            else {
                cout << s.top() << endl;
                s.pop();
            }
        } else if (cmd == "size") {
            cout << s.size() << endl;
        } else if (cmd == "empty") {
            cout << s.empty() << endl;
        } else if (cmd == "top") {
            if(s.size() == 0) cout << -1 << endl;
            else cout << s.top() << endl;
        }
    }

    return 0;
}
