
# [백준] 2003. 수들의 합 2

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2003) | 📁 분류: `투포인터` | ⭐ 난이도: `실버 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2180 KB |
|실행 시간| 0 ms |
|제출 일자|2026.03.31|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
```

### 입력
```text
4 2
1 1 1 1
```

### 출력
```text
3
```

-----

## 🧠 풀이 과정

### 0. 학습 방식

> ⚠️ 이 문제는 투 포인터 개념을 **처음 학습하면서** 참고하며 작성한 코드입니다.
> 블라인드 코딩이 아니라 개념을 보며 구현한 첫 연습이므로, 배운 점 위주로 정리합니다.

### 1. 처음 접근 방법

이중 루프로 `i`부터 `j`까지 전부 합산하는 완전탐색 O(N²)을 먼저 떠올렸으나,
N이 최대 10,000이므로 O(N) 방식인 투 포인터가 필요하다는 것을 학습했다.

### 2. 핵심 아이디어

`left`, `right` 두 포인터가 같은 방향으로 이동하며 구간 합을 유지한다.

| 조건 | 행동 |
|------|------|
| `sum == M` | count++ 후 left를 오른쪽으로 (구간 축소) |
| `sum < M`  | right를 오른쪽으로 (구간 확장) |
| `sum > M`  | left를 오른쪽으로 (구간 축소) |

**예시: N=4, M=2, 배열=[1,1,1,1]**

```
초기: left=0, right=0, sum=1

step1: sum(1) < M(2) → right=1, sum=2
step2: sum(2) == M   → count=1, left=1, sum=1
step3: sum(1) < M    → right=2, sum=2
step4: sum(2) == M   → count=2, left=2, sum=1
step5: sum(1) < M    → right=3, sum=2
step6: sum(2) == M   → count=3, left=3, sum=1
step7: sum(1) < M    → right=4 (N 초과 → 루프 종료)

결과: 3
```

두 포인터가 각각 최대 N번만 이동하므로 O(N)에 해결된다.

### 3. 시간/공간 복잡도 분析

- 시간 복잡도: `O(N)` — left, right 각각 최대 N번 이동
- 공간 복잡도: `O(N)` — 수열 저장 배열

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> array(N);
    for (int i = 0; i < N; i++) cin >> array[i];

    int left = 0, right = 0;
    long long sum = array[0];
    int count = 0;

    while (right < N) {
        if (sum == M) {
            count++;
            sum -= array[left++];
        } else if (sum < M) {
            right++;
            if (right < N) sum += array[right];
        } else {
            sum -= array[left++];
        }
    }

    cout << count;
    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

> 이 문제는 개념 학습 중 참고하며 작성했으므로 제출 오류는 없었습니다.
> 대신 처음에 헷갈렸던 부분을 정리합니다.

| 헷갈린 부분 | 내용 |
|------------|------|
| right 범위 초과 처리 | `right++` 후 `right < N`일 때만 sum에 더해야 함. 그냥 더하면 범위 초과 |
| sum 초기값 | `sum = 0`으로 시작하면 첫 번째 원소를 놓침. `sum = array[0]`으로 시작해야 함 |

### 상세 원인

```cpp
// ❌ 잘못된 패턴: right 범위 체크 없이 sum 증가
right++;
sum += array[right];  // right == N이면 범위 초과 (UB)

// ✅ 올바른 패턴
right++;
if (right < N) sum += array[right];
```

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 투 포인터 기본 템플릿 (연속 구간 합)

두 포인터가 같은 방향으로 이동하며 구간 합을 O(N)에 탐색하는 패턴.

```cpp
int left = 0, right = 0;
long long sum = array[0];

while (right < N) {
    if (sum == target) {
        // 정답 처리
        sum -= array[left++];   // 구간 축소
    } else if (sum < target) {
        right++;
        if (right < N) sum += array[right];  // 구간 확장
    } else {
        sum -= array[left++];   // 구간 축소
    }
}
```

**언제 쓰나:** 배열이 **양수**로만 이루어진 경우, 연속 부분합 관련 문제에서 사용.
(음수가 있으면 sum이 단조롭지 않아 투 포인터로 풀 수 없음)

### 2. 투 포인터가 O(N)인 이유

이중 루프처럼 보여도, left와 right가 **각각 0에서 N-1까지 한 번씩만** 이동하므로 총 연산은 최대 2N번 → O(N).
