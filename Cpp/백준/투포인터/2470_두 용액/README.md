
# [백준] 2470. 두 용액

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2470) | 📁 분류: `투포인터` | ⭐ 난이도: `골드 5`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2416 KB  |
|실행 시간| 12 ms   |
|제출 일자|2026.04.02|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
```

### 입력
```text
5
-2 4 -99 -1 98
```

### 출력
```text
-99 98
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

투포인터 문제임을 인식하고, 정렬 후 양 끝에 포인터를 두는 구조를 바로 떠올렸다.
- `sum > 0`이면 합을 줄여야 하니 `right--`
- `sum < 0`이면 합을 늘려야 하니 `left++`
- `sum == 0`이면 즉시 종료

알고리즘의 핵심 방향 자체는 처음부터 올바르게 잡았다.

### 2. 핵심 아이디어

배열을 정렬하면 **합이 너무 크면 right를 줄이고, 너무 작으면 left를 늘리는** 방식으로 O(N) 탐색이 가능하다.

예시: `[-99, -2, -1, 4, 98]` (정렬 후)

| 단계 | left | right | liquid[left] | liquid[right] | sum | 동작 |
|------|------|-------|-------------|--------------|-----|------|
| 1    | 0    | 4     | -99         | 98           | -1  | result=1, ans=(-99,98), left++ |
| 2    | 1    | 4     | -2          | 98           | 96  | abs(96)>1 → 갱신 안 함, right-- |
| 3    | 1    | 3     | -2          | 4            | 2   | abs(2)>1 → 갱신 안 함, right-- |
| 4    | 1    | 2     | -2          | -1           | -3  | abs(3)>1 → 갱신 안 함, left++ |
| 종료 | left >= right |

→ 최종 ans: `(-99, 98)` (합의 절댓값 1로 최솟값)

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N log N)` — 정렬 O(N log N) + 탐색 O(N)
- 공간 복잡도: `O(N)`

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 2470. 두 용액
- 분류: 투포인터
- 난이도: 골드 5
- 날짜: 2026.04.02
- 링크: https://www.acmicpc.net/problem/2470
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    vector<int> liquid;
    cin >> N;
    liquid.assign(N,0);

    for (int i = 0; i < N; i++) {
        cin >> liquid[i];
    }

    sort(liquid.begin(), liquid.end());

    int left = 0, right = N-1;
    int result = liquid[right] + liquid[left];
    pair<int, int> ans = {liquid[left], liquid[right]};
    while (left < right) {
        int sum = liquid[right] + liquid[left];

        if (sum == 0) {
            ans = {liquid[left], liquid[right]};
            break;
        } else if (sum > 0) {
            if (abs(result) > abs(sum)) {
                result = sum;
                ans = {liquid[left], liquid[right]};
            }
            right--;
        } else {
            if (abs(result) > abs(sum)) {
                result = sum;
                ans = {liquid[left], liquid[right]};
            }
            left++;
        }
    }

    cout << ans.first << " " << ans.second;

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|오답|`sum`에 `abs()` 적용 → 포인터 이동 방향 판단 불가|
|2차|오답|`left--` 오타 (`left++` 여야 함)|
|3차|오답|`result`, `ans` 초기화 누락|

### 상세 원인

**1차: `abs(sum)`으로 방향 판단 불가**

```cpp
// 잘못된 코드
int sum = abs(liquid[right] + liquid[left]);  // abs() 씌움

if (sum == 0) { ... }
else if (sum > 0) { right--; }  // 항상 여기만 실행됨
else { left--; }                // 절대 실행 안 됨
```

`abs()` 때문에 `sum`이 항상 0 이상이 되어, `left` 이동 분기가 dead code가 됨.

```cpp
// 수정
int sum = liquid[left] + liquid[right];  // abs() 제거
```

**2차: `left--` 오타**

포인터를 줄여야 할 이유가 없는데 `left--`로 작성해 잘못된 탐색 발생.

```cpp
// 잘못된 코드
left--;

// 수정
left++;
```

**3차: 초기값 설정 누락**

`result`와 `ans`를 초기화하지 않아, 루프에서 한 번도 갱신이 안 되면 쓰레기값 출력.

```cpp
// 잘못된 코드
int result = liquid[right] + liquid[left];  // abs 없이 음수 가능
pair<int, int> ans;                         // 초기화 없음

// 수정
int result = abs(liquid[left] + liquid[right]);
pair<int, int> ans = {liquid[left], liquid[right]};
```

### 개선점

- `abs()`는 방향 판단이 끝난 **후** 크기 비교에만 사용할 것
- 최솟값 추적 변수(`result`)와 정답 변수(`ans`)는 반드시 루프 진입 전에 초기화

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 투포인터에서 `abs()`는 비교에만, 방향 판단엔 쓰지 말 것

합의 부호로 포인터 방향을 결정하는 투포인터에서, `abs()`를 합 계산에 씌우면 방향 정보가 사라진다.

```cpp
int sum = liquid[left] + liquid[right];  // 부호 유지

if (sum > 0) right--;       // 합이 크면 right 감소
else if (sum < 0) left++;   // 합이 작으면 left 증가

// 최솟값 갱신할 때만 abs() 사용
if (abs(sum) < result) { result = abs(sum); ... }
```

### 2. 최솟값 추적 패턴: 초기값을 첫 번째 후보로 설정

`ans`처럼 함께 저장해야 하는 변수가 있을 때는 `INT_MAX` 대신 **첫 번째 후보값으로 초기화**하는 게 안전하다.

```cpp
int result = abs(liquid[left] + liquid[right]);
pair<int, int> ans = {liquid[left], liquid[right]};
```

### 3. `pair<int, int>`는 반드시 초기화할 것

`pair<int, int> ans;`처럼 선언만 하면 값이 초기화되지 않는다. 루프 내에서 한 번도 갱신 조건을 만족하지 못하면 쓰레기값이 그대로 출력된다.

```cpp
// 위험: 초기화 안 됨
pair<int, int> ans;

// 안전: 첫 번째 후보로 초기화
pair<int, int> ans = {liquid[left], liquid[right]};
```

정답을 저장하는 `pair`는 항상 의미 있는 초기값을 넣어두자.
