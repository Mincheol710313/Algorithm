
# [백준] 10866. 덱

> 🔗 [문제 링크](https://www.acmicpc.net/problem/10866) | 📁 분류: `자료구조` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |2024KB      |
|실행 시간|212ms      |
|제출 일자|2026.03.11|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
``` text
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
```

### 입력
``` text
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
```

### 출력
``` text
2
1
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

`deque`와 관련된 STL 라이브러리가 없다고 생각해서 `queue`를 이용하여 구현하여 문제 풀이를 하려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

`deque` STL 라이브러리를 이용하여 `deque` 자료구조를 사용하여 문제를 풀었다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(n)` - 입력받은 명령어 개수 `n`에 대하여 for문에서 처리한다.
- 공간 복잡도: `O(n)` - 최악의 경우, `push_front`/`push_back` 명령어가 n번 들어오는 경우 `deque`의 크기가 n이 된다.

-----

## 💻 최종 코드

```cpp
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
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|  False|  `size()`가 0일 때에도 `pop_front()`, `pop_back()`을 진행하게 Code를 작성해서 덱의 내부 상태가 망가져서 이상한 `size()`명령에 대해서 이상한 값을 반환함.|
|2차| Success| |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- STL 라이브러리 내에 `deque`이라는 라이브러리를 사용하면 간편하게 `deque` 자료구조를 사용할 수 있다.
