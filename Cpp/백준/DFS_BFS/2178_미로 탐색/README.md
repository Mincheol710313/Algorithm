
# [백준] 2178. 미로 탐색

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2178) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `실버 1`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2160 KB |
|실행 시간| 0 ms   |
|제출 일자|2026.04.03|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
N×M크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
```

### 입력
```text
4 6
101111
101010
101011
111011
```

### 출력
```text
15
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

최소 칸 수를 구하는 문제이므로 BFS를 사용하는 것이 맞다고 판단했다. 처음에는 큐에 좌표와 거리를 함께 `tuple<int,int,int>`로 묶어서 저장하고, 방문 처리를 `grid` 값을 0으로 덮어씌우는 방식으로 구현했다.

추가로 BFS 함수 내에서 `auto [y, x, d] = q.front()`로 구조 분해 할당을 했는데, 이 지역 변수 `y`, `x`가 전역 변수를 가리는 버그와 `dist` 배열 초기화 누락 버그가 있었다.

### 2. 핵심 아이디어

BFS는 같은 레벨(거리)의 노드를 먼저 모두 탐색하므로, 목적지에 처음 도달했을 때의 거리가 항상 최솟값이 된다.

`dist` 배열을 활용해 **큐에는 좌표만** 저장하고, 거리는 `dist[부모y][부모x] + 1`로 전파한다.

예시(4×6 미로) BFS 탐색 흐름:

```
시작: dist[0][0] = 1, q = [(0,0)]

(0,0) pop → 인접 (0,1) 방문: dist[0][1] = 2
(0,1) pop → 인접 (0,2) 방문: dist[0][2] = 3
...
(3,5) 도달 시: dist[3][5] = 15  ← 최솟값
```

방문 여부는 `dist[ny][nx] == 0`으로 판단 (0이면 미방문, 시작점은 1로 초기화).

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N×M)` — 각 칸을 최대 한 번씩 방문
- 공간 복잡도: `O(N×M)` — grid, dist 배열 + 큐

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int y, x;
vector<vector<int>> grid;
vector<vector<int>> dist;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

int bfs() {
    queue<tuple<int,int>> q;

    dist[0][0] = 1;
    q.push({0, 0});

    while (!q.empty()) {
        auto [cur_y, cur_x] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = cur_y + dy[i];
            int nx = cur_x + dx[i];

            if (inRange(ny, nx) && grid[ny][nx] == 1 && dist[ny][nx] == 0) {
                dist[ny][nx] = dist[cur_y][cur_x] + 1;
                q.push({ny, nx});
            }
        }
    }

    return dist[y-1][x-1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> y >> x;
    grid.assign(y, vector<int>(x, 0));
    dist.assign(y, vector<int>(x, 0));

    for (int i = 0; i < y; i++) {
        string nums;
        cin >> nums;
        for (int j = 0; j < x; j++) {
            grid[i][j] = nums[j] - '0';
        }
    }

    cout << bfs();

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|런타임 에러 / 오답|`dist` 배열 초기화 누락 + 전역 변수와 지역 변수 이름 충돌|
|2차|오답|큐에 거리를 같이 저장하고 `grid` 값으로 방문 처리 — 비정석적 구현|
|3차|정답|`dist[ny][nx] == 0`으로 방문 판단, 큐에 좌표만 저장|

### 상세 원인

**버그 1 — 전역 변수 shadowing**

```cpp
// 잘못된 코드
auto [y, x, d] = q.front();  // 전역 y, x를 가리는 지역 변수 생성
...
return dist[y-1][x-1];       // 마지막 pop된 좌표를 반환 → 오답

// 올바른 코드
auto [cur_y, cur_x] = q.front();  // 다른 이름 사용
...
return dist[y-1][x-1];            // 전역 y, x 정상 참조
```

**버그 2 — `dist` 배열 초기화 누락**

```cpp
// 잘못된 코드 (main에서)
grid.assign(y, vector<int>(x, 0));
// dist 초기화 없음 → dist[ny][nx] == 0 조건이 항상 true

// 올바른 코드
grid.assign(y, vector<int>(x, 0));
dist.assign(y, vector<int>(x, 0));  // 반드시 함께 초기화
```

### 개선점

- BFS 함수 안에서 전역 변수와 같은 이름의 지역 변수를 선언하지 않는다.
- `grid`, `dist` 등 쌍으로 사용하는 배열은 함께 초기화한다.

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 2D BFS 최단 거리 정석 패턴

큐에는 좌표만, 거리는 `dist` 배열로 관리한다. 방문 여부는 `dist == 0`으로 판단.

```cpp
queue<pair<int,int>> q;
dist[0][0] = 1;
q.push({0, 0});

while (!q.empty()) {
    auto [cy, cx] = q.front(); q.pop();
    for (int i = 0; i < 4; i++) {
        int ny = cy + dy[i];
        int nx = cx + dx[i];
        if (inRange(ny, nx) && grid[ny][nx] == 1 && dist[ny][nx] == 0) {
            dist[ny][nx] = dist[cy][cx] + 1;
            q.push({ny, nx});
        }
    }
}
```

### 2. DFS vs BFS 선택 기준

- **최솟값(최단 거리, 최소 칸 수)** 을 구해야 한다 → **BFS**
- **연결 여부, 연결 요소 개수** 를 구해야 한다 → DFS/BFS 모두 가능
