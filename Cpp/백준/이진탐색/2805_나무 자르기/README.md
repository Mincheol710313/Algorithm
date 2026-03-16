
# [백준] 2805. 나무 자르기

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2805) | 📁 분류: `이진탐색` | ⭐ 난이도: `실버 2`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 8296 KB |
|실행 시간| 156 ms |
|제출 일자|2026.03.16|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요

```text
상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
```

### 입력
``` text
4 7
20 15 10 17
```

### 출력
``` text
15
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

처음에는 단순하게 생각하여 저장되어 있는 나무의 높이 중에 하나를 절단기의 높이로 설정하면 답을 찾을 수 있다고 생각해서 `total` 값을 낼 수 있는 값을 이진 탐색을 이용하여 찾으려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

절단기는 저장되어 있는 나무의 높이가 아니여도 괜찮기 때문에 **1 ~ 최대 나무 높이**에서 필요한 나무 높이를 만족할 만한 절단기의 높이를 이진 탐색으로 찾아나가는 방식을 선택했다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(NlogN)` - `solution`함수 내부에서 이진 탐색하는데 `O(logN)`을 사용하고 `sum_height`에서 `O(N)`을 사용하기 때문에 합쳐서 `O(NlogN)`이 나온다. 
- 공간 복잡도: `O(N)` - 저장해야 하는 값의 최대 개수는 `tree_num`이기 때문에 `O(N)`이다.  

-----

## 💻 최종 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 2805. 나무 자르기
- 분류: 이진탐색
- 난이도: 실버 2
- 날짜: 2026.03.16
- 링크: https://www.acmicpc.net/problem/2805
*/
long long sum_height(vector<int>& v, int cut) {
    long long total_height = 0;
    for (int tree : v) {
        if (tree > cut) total_height += tree - cut;
    }
    return total_height;
}

int solution(vector<int>& v, long long target) {
    int start = 0, end = v.back();

    int answer;
    while (start <= end) {
        int mid = (start + end) / 2;
        
        long long total = sum_height(v, mid);
        if (total >= target) {
            answer = mid;
            start = mid +1;
        }
        else end = mid - 1;
    }

    return answer;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    
    int tree_num;
    long long need_height;
    cin >> tree_num >> need_height;

    vector<int> tree_heights;
    for (int i = 0; i < tree_num; i++) {
        int height;
        cin >> height;
        tree_heights.push_back(height);
    }
    
    sort(tree_heights.begin(), tree_heights.end());

    cout << solution(tree_heights, need_height);

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
| 1차| Fail| 기댓값이 출력되지 아예 출력되지 않음, 확인 결과 `end`와 `mid` 값이 잘못 설정되고 있어서 수정|
| 2차| Fail| 확인 결과 `total`을 `int`로 설정할 경우, **overflow**가 나올수 있는 상황이 있어서 `long long`으로 변경|
| 3차| Success| |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- 이진탐색에서 탐색 대상은 **배열 인덱스가 아니라 정답의 범위(값 자체)**여야 한다. 이 문제에서는 절단 높이(0 ~ max_height)를 탐색 범위로 설정해야 한다.
- 누적 합 계산 시 **오버플로우 주의**: N(최대 10^6) × 값(최대 10^9) = 최대 10^15로 `int` 범위(약 2×10^9)를 초과하므로 `long long`을 사용해야 한다.
- `int`로 선언된 변수에 21억을 초과하는 값이 누적되면 오버플로우로 음수 또는 쓰레기값이 된다.
