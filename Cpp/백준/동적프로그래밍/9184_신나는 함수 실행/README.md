
# [백준] 9184. 신나는 함수 실행

> 🔗 [문제 링크](https://www.acmicpc.net/problem/9184) | 📁 분류: `동적프로그래밍` | ⭐ 난이도: `실버 2`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2156 KB |
|실행 시간| 8 ms   |
|제출 일자|2026.04.09|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다.
a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
```

### 입력
```text
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
```

### 출력
```text
w(1, 1, 1) = 2
w(2, 2, 2) = 4
w(10, 4, 6) = 523
w(50, 50, 50) = 1048576
w(-1, 7, 18) = 1
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

시간 제한이 1초라 재귀만으로는 안 된다고 판단해 Memoization을 사용하려 했다.  
그런데 입력 범위가 `-50 ≤ a, b, c ≤ 50`이라서 배열 크기가 너무 커지는 게 아닐까 걱정했다.

### 2. 핵심 아이디어

**입력 범위와 실제 계산 범위는 다르다.**

함수 내부 조건을 보면:
- `a ≤ 0 || b ≤ 0 || c ≤ 0` → 즉시 1 반환 (재귀 없음)
- `a > 20 || b > 20 || c > 20` → `w(20, 20, 20)`으로 대체

즉, 입력이 -50~50이어도 **실제로 Memoization이 필요한 구간은 1~20뿐**이다.  
`dp[21][21][21]` = 9,261개로 충분하며 메모리도 약 9KB에 불과하다.

**재귀 호출 흐름 예시 (`w(2, 2, 2)` 계산):**

```
w(2, 2, 2)
  └─ a < b && b < c 조건 불만족 → otherwise 분기
     = w(1,2,2) + w(1,1,2) + w(1,2,1) - w(1,1,1)
          │         │
          │         └─ 이미 계산됐으면 dp에서 바로 반환
          └─ 처음 호출이면 계산 후 dp에 저장
```

한 번 계산한 `w(1,1,1)`은 이후 호출에서 dp에서 O(1)로 반환되므로 중복 계산이 없다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(20³)` — 각 상태(a, b, c)는 최대 한 번만 계산
- 공간 복잡도: `O(20³)` — dp 배열 크기

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

int a, b, c;
vector<vector<vector<int>>> dp;

int w(int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) return 1;
    if (a > 20 || b > 20 || c > 20) return w(20, 20, 20);

    if (dp[a][b][c] != -1) return dp[a][b][c];

    if (a < b && b < c)
        return dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);

    return dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    dp.assign(21, vector<vector<int>>(21, vector<int>(21, -1)));

    while (true) {
        cin >> a >> b >> c;
        if (a == -1 && b == -1 && c == -1) break;
        cout << "w(" << a << ", " << b << ", " << c << ") = " << w(a, b, c) << "\n";
    }

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|벡터 선언 오류|`vector<int, vector<int, vector<int>>>`로 잘못 선언|

### 상세 원인

`vector`의 두 번째 템플릿 인자는 **allocator**용이라 중첩 벡터 선언에 쓸 수 없다.

```cpp
// 잘못된 선언
vector<int, vector<int, vector<int>>> dp;

// 올바른 선언
vector<vector<vector<int>>> dp;
```

### 개선점

- 3D 벡터 선언 시 `vector<vector<vector<T>>>`처럼 꺾쇠를 중첩해야 한다.
- Memoization 초기값은 유효한 반환값과 겹치지 않는 `-1`을 사용한다.

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. Memoization vs Tabulation 차이

DP를 구현하는 방식은 두 가지로 나뉜다.

| | Memoization (Top-down) | Tabulation (Bottom-up) |
|--|--|--|
| **방향** | 큰 문제 → 작은 문제 (재귀) | 작은 문제 → 큰 문제 (반복문) |
| **계산** | 필요한 것만 계산 | 모든 경우를 미리 계산 |
| **구현** | 재귀 + dp 배열 | 반복문 + dp 배열 |
| **장점** | 불필요한 계산 없음 | 재귀 오버헤드 없음 |

```cpp
// Memoization: 호출될 때 계산하고 저장
int w(int a, int b, int c) {
    if (dp[a][b][c] != -1) return dp[a][b][c]; // 이미 계산했으면 바로 반환
    return dp[a][b][c] = /* 계산 */;            // 처음이면 계산 후 저장
}

// Tabulation: 미리 모든 경우를 채워둠
for (int i = 0; i <= 20; i++)
    for (int j = 0; j <= 20; j++)
        for (int k = 0; k <= 20; k++)
            dp[i][j][k] = /* 계산 */;
```

이 문제는 재귀 구조가 명확하고 불필요한 계산을 줄일 수 있어 **Memoization이 자연스럽다.**

### 2. 입력 범위 ≠ 실제 계산 범위

입력이 넓어도 함수 내부 조건이 범위를 클램핑하는 경우,  
**실제 dp 배열 크기는 클램핑 범위 기준으로 잡으면 된다.**

```cpp
if (a > 20 || b > 20 || c > 20) return w(20, 20, 20); // 20 초과는 모두 동일
// → dp[21][21][21]로 충분
```

### 3. Memoization sentinel 값

초기값은 유효한 반환값과 **반드시 달라야** 한다.

```cpp
dp.assign(21, vector<vector<int>>(21, vector<int>(21, -1))); // -1로 초기화
if (dp[a][b][c] != -1) return dp[a][b][c];                  // -1이면 아직 미계산
```
