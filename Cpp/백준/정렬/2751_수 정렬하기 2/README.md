
# [백준] 2751. 수 정렬하기 2

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2751) | 📁 분류: `정렬` | ⭐ 난이도: `실버 5`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 8296 KB |
|실행 시간| 252 ms |
|제출 일자|2026.03.13|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
``` text
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
```

### 입력
``` text
5
5
4
3
2
1
```
### 출력
``` text
1
2
3
4
5
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

수 정렬 문제이기 때문에 STL `sort()` 함수를 이용해서 문제를 풀이

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

최악의 경우에도 `O(NlogN)`을 만족하는 STL `sort`함수를 이용하여 `vector`를 정렬

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(NlogN)` - STL sort 알고리즘은 최악의 경우에도 `O(NlogN)`을 보장
- 공간 복잡도: `O(N)` - 입력받는 수의 개수가 N개

-----

## 💻 최종 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
- [백준] 2751. 수 정렬하기 2
- 분류: 정렬
- 난이도: 실버 5
- 날짜: 2026.03.13
- 링크: https://www.acmicpc.net/problem/2751
*/

void bubble_sort(vector<int>& v, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - 1 -i; j++) {
            if (v[j] > v[j+1]) swap(v[j], v[j+1]);
        }
    }
}

void quick_sort(vector<int>& v, int start, int end) {
    if (start >= end) return;
    int pivot = start;
    int left = start + 1;
    int right = end;

    while (left <= right) {
        while (left <= end && v[left] <= v[pivot]) left += 1;
        while (right > start && v[right] >= v[pivot]) right -= 1;
        
        if(left > right) {
            swap(v[right], v[pivot]);
        } else {
            swap(v[right], v[left]);
        }
    }

    quick_sort(v, start, right-1);
    quick_sort(v, right+1, end);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;

    vector<int> v;

    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;

        v.push_back(num);
    }

    // bubble_sort(v, N);
    // quick_sort(v, 0, N-1);
    sort(v.begin(), v.end());

    for (int i = 0; i < N; i++) {
        cout << v[i] << "\n";
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

- Quick Sort와 Bubble Sort를 직접 구현해보면서 Sort Algorithm에 대해서 공부하였다.
