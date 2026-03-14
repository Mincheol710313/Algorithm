
# [백준] 7795. 먹을 것인가 먹힐 것인가

> 🔗 [문제 링크](https://www.acmicpc.net/problem/7795) | 📁 분류: `이진탐색` | ⭐ 난이도: `실버 3`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2408 KB |
|실행 시간| 28 ms |
|제출 일자|2026.03.14|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요

``` text
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.
두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 
```

### 입력
``` text
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
```

### 출력
``` text
7
1
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

사냥꾼의 크기보다 작은 크기를 가진 사냥감의 개수를 찾는 것이기 때문에 결국 이진 탐색(Binary Search)를 사용하여 문제를 해결하려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

이진 탐색(Binary Search)와 관련한 STL 라이브러리의 `upper_bound`와 `lower_bound` 함수를 이용해서 사낭꾼의 크기보다 **처음으로 크거나 같은** 정렬된 사냥감의 개수를 찾아서 문제를 해결했다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(NlogN)` - `lower_bound`의 시간 복잡도는 `O(logN)`이다. 그렇기 때문에 탐색의 시간 복잡도는 `O(NlogN)` 수준이고 `sort` 알고리즘의 시간 복잡도도 `O(NlogN)`이기 때문에 전체 시간 복잡도는 `O(NlogN)` 수준이다. 
- 공간 복잡도: `O(N)` - Hunter 혹은 Prey 중 최대의 개수만 고려했을 때, `O(N)` 수준이다.

-----

## 💻 최종 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 7795. 먹을 것인가 먹힐 것인가
- 분류: 이진탐색
- 난이도: 실버 3
- 날짜: 2026.03.14
- 링크: https://www.acmicpc.net/problem/7795
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int test_num;
    cin >> test_num;

    for (int i = 0; i < test_num; i++) {
        int hunter_num, prey_num;
        cin >> hunter_num >> prey_num;

        vector<int> hunters, preys;
        for (int j = 0; j < hunter_num; j++) {
            int hunter;
            cin >> hunter;
            hunters.push_back(hunter);
        }

        for (int j = 0; j < prey_num; j++) {
            int prey;
            cin >> prey;
            preys.push_back(prey);
        }

        sort(preys.begin(), preys.end());

        int total = 0;
        for (int hunter : hunters) {
            total += lower_bound(preys.begin(), preys.end(), hunter) - preys.begin();
        }

        cout << total << "\n";
    }
    
    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|  Success|  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- 이진 탐색(Binary Search)와 관련된 문제가 나왔을 때, 직접 함수를 구현해도 좋지만, STL `<algorithm>`에서 제공하는 `lower_bound`와 `upper_bound`함수를 이용해보자.
