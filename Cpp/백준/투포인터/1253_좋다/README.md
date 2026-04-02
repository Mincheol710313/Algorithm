
# [백준] 1253. 좋다

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1253) | 📁 분류: `투포인터` | ⭐ 난이도: `골드 4`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2024 KB |
|실행 시간| 12 ms |
|제출 일자|2026.04.02|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.
```

### 입력
```text
10
1 2 3 4 5 6 7 8 9 10
```

### 출력
```text
8
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

각 수를 `target`으로 정하고, 나머지 수 중 두 개의 합이 `target`이 되는지 투포인터로 확인하는 구조를 바로 떠올렸다.
- 정렬 후 `left=0`, `right=N-1`에서 시작
- `sum < target`이면 `left++`, `sum > target`이면 `right--`
- `sum == target`이면 좋은 수

투포인터의 핵심 방향 판단은 처음부터 올바르게 잡았다.

### 2. 핵심 아이디어

각 `arr[i]`를 target으로 두고, 투포인터로 `arr[left] + arr[right] == target`을 탐색한다.
단, **자기 자신(`i`)을 합의 재료로 쓰면 안 된다**는 조건이 핵심이다.

예시: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, target = `3` (index 2)

| 단계 | left | right | sum | 동작 |
|------|------|-------|-----|------|
| 1    | 0    | 9     | 11  | right-- |
| 2    | 0    | 8     | 10  | right-- |
| ...  | ...  | ...   | ... | ... |
| k    | 0    | 2     | 4   | right-- |
| k+1  | 0    | 1     | 3   | sum==target, left(0)≠2, right(1)≠2 → count++ |

예시: target = `2` (index 1)

| 단계 | left | right | sum | 동작 |
|------|------|-------|-----|------|
| 1    | 0    | 9     | 11  | right-- |
| ...  | ...  | ...   | ... | ... |
| k    | 0    | 1     | 3   | right-- |
| k+1  | 0    | 1     | sum==target이지만 right==i(1) → right-- |
| k+2  | 0    | 0     | left >= right → 종료 (좋은 수 아님) |

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N^2)` — N개의 target마다 투포인터 O(N)
- 공간 복잡도: `O(N)`

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 1253. 좋다
- 분류: 투포인터
- 난이도: 골드 4
- 날짜: 2026.04.02
- 링크: https://www.acmicpc.net/problem/1253
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int N;
    vector<int> arr;
    cin >> N;
    arr.assign(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    int count = 0;
    for (int i = 0; i < N; i++) {
        int target = arr[i];

        int left = 0, right = N-1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            
            if (sum == target) {
                if(left != i && right != i) {
                    count++;
                    break;
                } else if (left == i) {
                    left++;
                } else {
                    right--;
                }   
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    cout << count;

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|입력 대기(무한 대기)|입력 받는 코드 누락|
|2차|오답|자기 자신을 합의 재료로 사용하는 경우를 걸러내지 않음|

### 상세 원인

**1차: 입력 코드 누락**

```cpp
// 잘못된 코드
arr.assign(N, 0);
// 입력 받는 for문 없음
sort(arr.begin(), arr.end());

// 수정
for (int i = 0; i < N; i++) cin >> arr[i];
```

**2차: 자기 자신 인덱스 미제외**

`arr[i] = 4`이고 `arr[2] + arr[2] = 4`처럼 같은 인덱스를 두 번 쓰는 경우를 허용하면 오답.

```cpp
// 잘못된 코드
if (sum == target) {
    count++;
    break;
}

// 수정: left 또는 right가 i와 같으면 포인터를 한 칸 이동
if (sum == target) {
    if (left != i && right != i) {
        count++;
        break;
    } else if (left == i) left++;
    else right--;
}
```

### 개선점

- 투포인터로 특정 원소를 제외하고 탐색할 때는 `left != i && right != i` 조건을 반드시 확인

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 자기 자신 인덱스 제외 패턴

투포인터로 "다른 두 수의 합"을 찾을 때, `left`나 `right`가 자기 자신 인덱스(`i`)를 가리키면 건너뛰어야 한다.

```cpp
if (sum == target) {
    if (left != i && right != i) {
        count++;
        break;
    } else if (left == i) left++;
    else right--;
}
```

### 2. 외부 루프 + 내부 투포인터 구조

"N개 각각에 대해 조건을 만족하는 쌍이 존재하는지" 확인할 때 이 구조를 써먹을 수 있다.

```cpp
for (int i = 0; i < N; i++) {       // 각 원소를 target으로
    int left = 0, right = N - 1;
    while (left < right) {           // 투포인터로 나머지 탐색
        ...
    }
}
```
