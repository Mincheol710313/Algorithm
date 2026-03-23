
# [백준] 1697. 숨바꼭질

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1697) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `실버 1`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |2544 KB      |
|실행 시간|0 ms      |
|제출 일자|2026.03.23|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때, 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하시오.
```

### 입력
```text
5 17
```

### 출력
```text
4
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

처음에는 DFS나 단순 탐색으로 접근하려 했지만, 최소 시간을 구해야 한다는 조건 때문에 어떤 탐색을 써야 할지 바로 떠오르지 않았다.

### 2. 핵심 아이디어

각 위치를 **노드**, 이동(X-1, X+1, 2X)을 **엣지**로 보면 그래프 탐색 문제가 된다.
모든 이동의 비용이 **1초로 동일**하므로, **가중치 없는 그래프의 최단 경로 = BFS**가 된다.

BFS는 거리 순서대로 탐색하기 때문에, K에 처음 도달하는 순간이 곧 최소 시간이 된다.

```
1초: {4, 6, 10}
2초: {3, 5, 7, 8, 9, 11, 12, 20} ...
3초: ...
4초: ... 17 도달!
```

DFS를 쓰면 처음 K에 도달해도 그게 최단인지 보장할 수 없다.

| | DFS | BFS |
|--|--|--|
| 최단 보장 | X | O (가중치 동일 시) |
| 이 문제에 적합? | X | O |

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N)` — 최대 위치가 100,000이므로 노드 수 = 100,001
- 공간 복잡도: `O(N)` — visited 배열 및 큐

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

#define MAX 100001

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int subin, brother;
    cin >> subin >> brother;

    queue<int> q;
    vector<int> dist(MAX, -1);
    q.push(subin);
    dist[subin] = 0;

    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        if(cur == brother) {
            cout << dist[brother];
            break;
        }
        for(int next : {cur - 1, cur + 1, cur*2}) {
            if(next >= 0 && next < MAX && dist[next] == -1) {
                dist[next] = dist[cur] + 1;
                q.push(next);
            }
        }
    }

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|  |  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. "최소 횟수/시간" + 균일한 이동 비용 → BFS

문제에서 **최소 횟수, 최소 시간**이 나오고, 각 이동의 비용이 동일하다면 BFS가 정답이다.
BFS는 레벨(거리) 순서로 탐색하므로, 목적지에 처음 도달한 순간이 최단임을 보장한다.

```cpp
queue<int> q;
vector<int> dist(MAX, -1);
q.push(start);
dist[start] = 0;

while (!q.empty()) {
    int cur = q.front(); q.pop();
    if (cur == target) { cout << dist[cur]; break; }
    for (int next : {cur-1, cur+1, cur*2}) {
        if (next >= 0 && next < MAX && dist[next] == -1) {
            dist[next] = dist[cur] + 1;
            q.push(next);
        }
    }
}
```
