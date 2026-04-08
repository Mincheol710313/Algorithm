
# [백준] 1003. 피보나치 함수

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1003) | 📁 분류: `동적프로그래밍` | ⭐ 난이도: `실버 3`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2020 KB  |
|실행 시간| 0 ms    |
|제출 일자|2026.04.08|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
```

### 입력
```text
3
0
1
3
```

### 출력
```text
1 0
0 1
1 2
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

전역 변수 `zero_count`, `one_count`를 두고 재귀 함수 내에서 베이스 케이스 도달 시 증가시키는 방식을 먼저 시도했다.

```cpp
int zero_count = 0, one_count = 0;

int fib(int n) {
    if (n == 0) { zero_count++; return 0; }
    else if (n == 1) { one_count++; return 1; }
    else return fib(n-1) + fib(n-2);
}
```

이 방법은 로직은 맞지만, 제한 시간이 **0.25초**인 것을 보고 재귀 방식으로는 TLE임을 파악했다. `N ≤ 40`, `T ≤ 1000`일 때 `fib(40)` 순수 재귀는 약 2억 번 호출, T=1000이면 총 2000억 번 → 불가능.

### 2. 핵심 아이디어

`fib(n)` 호출 시 0과 1이 출력되는 횟수를 DP 배열로 미리 계산한다.

```
zero[n] = fib(n) 호출 시 0이 출력되는 횟수
one[n]  = fib(n) 호출 시 1이 출력되는 횟수
```

`fib(n) = fib(n-1) + fib(n-2)` 이므로, 각 카운트도 같은 점화식을 따른다.

```
zero[0] = 1,  zero[1] = 0
one[0]  = 0,  one[1]  = 1

zero[n] = zero[n-1] + zero[n-2]  (n >= 2)
one[n]  = one[n-1]  + one[n-2]   (n >= 2)
```

단계별 계산:

| n | zero[n] | one[n] |
|---|---------|--------|
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 1 |
| 3 | 1 | 2 |
| 4 | 2 | 3 |
| 5 | 3 | 5 |

N=0~40까지 **O(40)** 전처리 후, 각 테스트케이스는 **O(1)** 조회.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(40 + T)` → 사실상 `O(1)`
- 공간 복잡도: `O(40)` (DP 배열)

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

int T, N;
vector<int> zero_count;
vector<int> one_count;

void fib() {
    zero_count[0] = 1; zero_count[1] = 0;
    one_count[0] = 0;  one_count[1] = 1;

    for (int i = 2; i < 41; i++) {
        zero_count[i] = zero_count[i-1] + zero_count[i-2];
        one_count[i]  = one_count[i-1]  + one_count[i-2];
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    zero_count.assign(41, 0);
    one_count.assign(41, 0);
    fib();

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        cout << zero_count[N] << " " << one_count[N] << "\n";
    }

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|런타임 에러|`one_count.assign()` 대신 `zero_count.assign()`을 두 번 작성하여 `one_count` 벡터 크기가 0인 채로 접근|

### 상세 원인

```cpp
// 잘못된 코드
zero_count.assign(41, 0);
zero_count.assign(41, 0);  // ← one_count가 되어야 함

// 올바른 코드
zero_count.assign(41, 0);
one_count.assign(41, 0);
```

`one_count`가 초기화되지 않아 크기 0인 상태에서 `fib()` 내부의 `one_count[0]` 접근 시 **out of range** 런타임 에러 발생.

### 개선점

- 같은 이름의 변수를 여러 개 초기화할 때 복붙 후 변수명 수정을 꼭 확인한다.

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 시간 제한으로 알고리즘 방향 파악하기

제한 시간이 0.25초처럼 타이트하면 지수 시간 재귀는 불가능하다. 재귀로 구조를 파악한 뒤 DP로 전환하는 패턴을 바로 적용한다.

| 방식 | fib(40) 호출 수 | T=1000 전체 |
|------|--------------|------------|
| 순수 재귀 | ~2억 번 | ~2000억 번 (TLE) |
| DP 전처리 | 40번 | 40 + 1000번 (O(1)) |

### 2. 재귀 카운트를 DP로 변환하기

`fib(n)` 호출 시 베이스 케이스 도달 횟수도 같은 점화식을 따른다. 재귀 함수의 카운팅 문제는 카운트 배열을 별도로 선언해 DP로 미리 계산해두면 된다.

```cpp
// 점화식 패턴
count[0] = base0;
count[1] = base1;
for (int i = 2; i <= MAX; i++)
    count[i] = count[i-1] + count[i-2];
```
