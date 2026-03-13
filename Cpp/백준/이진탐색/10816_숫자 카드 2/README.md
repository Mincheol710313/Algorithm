
# [백준] 10816. 숫자 카드 2

> 🔗 [문제 링크](https://www.acmicpc.net/problem/10816) | 📁 분류: `이진탐색` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 23304KB |
|실행 시간| 356ms |
|제출 일자|2026.03.13|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요

``` text
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
```

### 입력

``` text
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
```

### 출력

``` text
3 0 0 1 2 0 0 2 
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

처음에는 카드 찾는 것을 중점으로 생각하여서 Binary Search를 이용하려고 했다. 하지만 실제로 중요한 것은 **몇 개** 가지고 있는 지 구하는 것이기 때문에 **Hash** 자료구조를 이용하는 풀이로 변경했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

Hash에 현재 상근이가 가지고 있는 카드와 해당 카드의 개수를 저장하는 것이 핵심이다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N)` - 기본적으로 상근이가 가지고 있는 카드 N개에 대해서 Hash에 저장해야 하기 때문에
- 공간 복잡도: `O(N)` - 만약 상근이가 가지고 있는 카드가 모두 다른 경우라면 N개를 저장해야 하기 때문에

-----

## 💻 최종 코드

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

/*
- [백준] 10816. 숫자 카드 2
- 분류: 이진탐색
- 난이도: 실버 4
- 날짜: 2026.03.13
- 링크: https://www.acmicpc.net/problem/10816
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_count;
    cin >> num_count;

    unordered_map<int,int> number_counts;

    for (int i = 0; i < num_count; i++) {
        int num;
        cin >> num;
        if (number_counts.find(num) == number_counts.end()) number_counts[num] = 1;
        else number_counts[num] += 1;
    }

    int check_count;
    cin >> check_count;

    for (int i = 0; i < check_count; i++) {
        int check_num;
        cin >> check_num;
        if (number_counts.find(check_num) == number_counts.end()) cout << 0 << " ";
        else cout << number_counts[check_num] << " ";
    }

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차| Success|  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- Hash에 Key 값이 있는지 확인하는 방법 : `number_counts.find(check_num) == number_counts.end()`
