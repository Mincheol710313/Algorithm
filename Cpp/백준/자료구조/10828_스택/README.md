
# [백준] 10828. 스택

> 🔗 [문제 링크](https://www.acmicpc.net/problem/10828) | 📁 분류: `자료구조` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |  2204 KB|
|실행 시간|  212 ms|
|제출 일자|2026.03.11|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
```

### 입력
```text
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```

### 출력
```
2
2
0
2
1
-1
0
1
-1
0
3
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

기본적으로 문제가 `stack`을 구현하거나 사용할 수 있는지 물어보는 문제이기 때문에 처음에는 `vector`를 이용해서 `stack`의 기능을 구현하려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

실질적으로 문제를 풀 때에는 `stack` STL 라이브러리를 이용하여 `stack`을 만든 후에 `stack`의 메서드를 이용해서 문제를 해결했다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(n)` - 명령어를 for문을 통해서 처리
- 공간 복잡도: `O(n)` - 최악의 상황에서 push가 n번 일어날 경우, stack의 길이가 n

-----

## 💻 최종 코드

```cpp
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
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|  |  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

-
