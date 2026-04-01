
# [백준] 1806. 부분 합

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1806) | 📁 분류: `투포인터` | ⭐ 난이도: `골드 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2412 KB      |
|실행 시간| 8 ms      |
|제출 일자|2026.04.01|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
```

### 입력
```text
10 15
5 1 3 5 10 7 4 9 2 8
```

### 출력
```text
2
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

left, right 두 포인터를 0에서 시작하고, `sum >= S`이면 길이를 갱신하면서 left를 줄이고, `sum < S`이면 right를 늘리는 방식으로 접근했다.

### 2. 핵심 아이디어

투포인터에서 **while문 내부 조건 분기**가 핵심이다.

- `sum >= S`: 조건 만족 → 길이 갱신 후 left를 오른쪽으로 이동 (범위 축소)
- `sum < S`: 조건 미만 → right를 오른쪽으로 이동 (범위 확장)
- while 종료 조건: `right < N`

이렇게 하면 left/right 각각 최대 N번 이동하므로 전체 `O(N)`에 해결된다.

**단계별 포인터 변화 (예시: `5 1 3 5 10 7 4 9 2 8`, S=15)**

| 단계 | left | right | 구간 합 | 동작 |
|------|------|-------|---------|------|
| 1 | 0 | 0 | 5 | sum<15 → right++ |
| 2 | 0 | 1 | 6 | sum<15 → right++ |
| 3 | 0 | 2 | 9 | sum<15 → right++ |
| 4 | 0 | 3 | 14 | sum<15 → right++ |
| 5 | 0 | 4 | 24 | sum>=15 → length=5, left++ |
| 6 | 1 | 4 | 19 | sum>=15 → length=4, left++ |
| 7 | 2 | 4 | 18 | sum>=15 → length=3, left++ |
| 8 | 3 | 4 | 15 | sum>=15 → length=2, left++ |
| 9 | 4 | 4 | 10 | sum<15 → right++ |
| 10 | 4 | 5 | 17 | sum>=15 → length=2, left++ |
| ... | ... | ... | ... | ... |
| 최종 | - | - | - | **length = 2** |

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N)` — left, right 각각 최대 N번 이동
- 공간 복잡도: `O(N)` — 수열 저장 배열

-----

## 💻 최종 코드

```cpp
int main() {
    int N, S;
    vector<int> arr;
    cin >> N >> S;
    arr.assign(N, 0);
    for (int i = 0; i < N; i++) cin >> arr[i];

    int left = 0, right = 0;
    int length = 0;   // 0: 아직 조건 만족한 구간 없음 (= 정답이 없으면 0 출력)
    int sum = arr[0];

    while (right < N) {
        if (sum >= S) {
            if (length == 0) length = right - left + 1;
            else length = min(length, right - left + 1);
            sum -= arr[left++];
        } else {
            right++;
            if (right < N) sum += arr[right];
        }
    }

    cout << length;  // 조건 만족 없으면 그대로 0 출력
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|틀렸습니다 (19%)|`length = -1`로 초기화 → 조건 불만족 시 -1 출력|
|2차|맞았습니다|`length = 0`으로 초기화 → 자연스럽게 0 출력|

### 상세 원인

문제 조건: **만약 그런 것이 없다면 0을 출력**

처음에 `length = -1`로 초기화했더니, 조건을 만족하는 구간이 없을 때 -1이 그대로 출력됐다.

```cpp
// 틀린 코드
int length = -1;
...
cout << length;  // 조건 불만족 시 -1 출력

// 고친 코드
int length = 0;
...
if (length == 0) length = right - left + 1;  // 첫 갱신
else length = min(length, right - left + 1);
...
cout << length;  // 조건 불만족 시 자연스럽게 0 출력
```

`-1`로 두고 출력 시점에 `(length == -1 ? 0 : length)`로 변환하는 방법도 있지만,
`0`을 sentinel로 쓰면 출력을 그대로 `cout << length`로 쓸 수 있어서 더 깔끔하다.

이게 가능한 이유: **유효한 부분합의 최솟값 길이는 1 이상**이므로 0과 혼동될 일이 없다.

### 개선점

"없으면 X를 출력" 조건이 있을 때, X 자체를 sentinel 초기값으로 쓸 수 있는지 먼저 고민할 것.

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 투포인터 while문 구조

투포인터의 핵심은 **while문 내부를 조건에 따라 명확히 분기**하는 것이다.

```cpp
while (right < N) {
    if (조건 만족) {
        // 정답 갱신
        // left 이동 (범위 축소)
        sum -= arr[left++];
    } else {
        // right 이동 (범위 확장)
        right++;
        if (right < N) sum += arr[right];
    }
}
```

- 조건 만족 시 → 최솟값 갱신 + left 좁히기
- 조건 미만 시 → right 확장
- 이 구조만 잘 잡으면 O(N)으로 최솟값/최댓값 구하는 문제 대부분 해결 가능

### 2. "없으면 X 출력"은 X를 sentinel로 활용

최솟값을 구하는 문제에서 sentinel로 INT_MAX나 -1을 쓰면 출력 시 변환이 필요하다.  
**정답이 없을 때 출력해야 할 값(0 등)이 유효한 정답 범위 밖이라면, 그 값 자체를 sentinel로 쓰는 게 더 깔끔하다.**

```cpp
int length = 0;  // "없으면 0 출력" → 0을 sentinel로 초기화

if (length == 0) length = right - left + 1;  // 첫 갱신
else length = min(length, right - left + 1);

cout << length;  // 변환 없이 그대로 출력
```
