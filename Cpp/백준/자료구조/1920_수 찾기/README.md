
# [백준] 1920. 수 찾기

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1920) | 📁 분류: `자료구조` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 6820KB|
|실행 시간| 56ms|
|제출 일자|2026.03.12|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
```

### 입력
```text
5
4 1 5 2 3
5
1 3 7 9 5
```

### 출력
```text
1
1
0
0
1
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

처음에는 `Set(집합)`을 이용해서 문제 풀이를 진행하려고 했지만, 알고리즘에 Hash와 Map이라는 분류가 있어서 가장 기본적인 `unordered_map`을 이용하여 문제를 풀게 되었다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

`unordered_map`에서 Key를 찾을 때에는 `O(1)`에 해당하는 시간이 걸리기 때문에 값들을 Key로 저장하고 있다면 아주 빠르게 찾을 수 있다. 그래서 이분 탐색과 같은 알고리즘을 사용하지 않고 빠르게 값을 찾을 수 있는 `unordered_map`자료구조를 사용해서 문제를 풀었다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N)` - N개에 대해서 입력을 받고 M개에 대해서 파악을 하는 것이기 때문에 O(N+M)이지만 단순하게 O(N)으로 파악할 수 있다.
- 공간 복잡도: `O(N)` - Map에 N개의 쌍이 들어가기 때문에 O(N)으로 파악할 수 있다.

-----

## 💻 최종 코드

```cpp
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
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차| False| `endl`은 출력 후 버퍼를 강제로 flush하기 때문에, I/O가 매우 느려진다.|
|2차| Success| |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- Coding Test에서 `endl`을 사용하는 것은 좋지 않다. 줄바꿈 + **버퍼 flush**가 이루어지기 때문에 속도가 느려진다. 그래서 줄바꿈만 필요하다면 `"\n"`을 사용하는 것이 좋다.
- Hash 사용하는 방법 정리
