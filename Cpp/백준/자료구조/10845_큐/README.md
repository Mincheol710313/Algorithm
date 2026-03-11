
# [백준] 10845. 큐

> 🔗 [문제 링크](https://www.acmicpc.net/problem/10845) | 📁 분류: `자료구조` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |  2024 KB|
|실행 시간|  208 ms|
|제출 일자|2026.03.11|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
``` text
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
```

### 입력
``` text
15
push 1
push 2
front
back
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
front
```

### 출력
``` text
1
2
2
0
1
2
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

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(n)` - N개의 명령을 for문을 통해서 처리
- 공간 복잡도: `O(n)` - 최악의 경우 N번 모두 push면 큐에 N개 저장

-----

## 💻 최종 코드

```cpp
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
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|  |  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- Queue는 `front()`로 읽고 `pop()`으로 제거해야 한다.
- C++에서 `cin`이 공백을 자동 구분자로 처리하기 때문에 한 줄에 2개 이상을 입력 받을 때 굳이 두 개를 동시에 받아서 처리할 필요 없다. `cin >> a >> b`처럼 연속으로 받으면 공백/줄바꿈을 자동으로 건너뛰며 순서대로 읽는다.
