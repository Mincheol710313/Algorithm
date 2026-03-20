
# [백준] 2206. 벽 부수고 이동하기

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2206) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `골드 3`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |62496 KB      |
|실행 시간|288 ms      |
|제출 일자|2026.03.20|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고,
1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데,
이때 최단 경로로 이동하려 한다.
최단 경로는 맵에서 가장 적은 개수의 칸을 지나는 경로인데,
이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
한 개까지 벽을 부수고 이동할 수 있다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
```

### 입력
```text
6 4
0100
1110
1000
0000
0111
0000
```

### 출력
```text
15
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

처음에는 DFS로 풀려고 했다. 하지만 맵 크기가 최대 1000×1000이라 DFS로 모든 경로를 탐색하면 시간 초과가 발생한다. 최단 경로 문제이므로 BFS가 적합하다.

### 2. 핵심 아이디어

**상태 BFS**: 단순히 좌표만 저장하는 게 아니라 **"벽을 부쉈는지 여부"** 도 상태로 관리한다.

`dist[y][x][broke]`를 3D 배열로 선언한다.
- `broke = 0`: 벽을 아직 부수지 않은 상태로 `(y, x)`에 도달했을 때 거리
- `broke = 1`: 벽을 1번 부수고 `(y, x)`에 도달했을 때 거리

BFS 큐에도 `(y, x, broke)` 세 값을 함께 저장해야 꺼낼 때 현재 상태를 알 수 있다.

이동할 때 조건:

| 다음 칸 | broke 상태 | 처리 |
|--------|-----------|------|
| 빈 칸(0) | 0 | `dist[ny][nx][0]` 미방문이면 그대로 이동 |
| 벽(1) | 0 | `dist[ny][nx][1]` 미방문이면 벽 부수고 이동 (broke → 1) |
| 빈 칸(0) | 1 | `dist[ny][nx][1]` 미방문이면 이동 (벽 이미 부쉈으므로 벽은 못 부숨) |

**큐 상태 변화 예시** (1.in 기준, 6×4 맵):

```
맵:
0 1 0 0
1 1 1 0
1 0 0 0
0 0 0 0
0 1 1 1
0 0 0 0

(0,0) broke=0, dist=1
→ (0,1) 벽 → broke=1, dist=2
  → (0,2) 빈칸 → broke=1, dist=3
    → (0,3) 빈칸 → broke=1, dist=4
      → (1,3) 빈칸 → broke=1, dist=5
        ...
→ (1,0) 벽이지만 broke=0이므로 부수고 이동 가능
  → 다른 경로 탐색...

최종: dist[5][3][1] = 15
```

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N × M)` — 각 칸을 broke 상태 2가지로 최대 2번 방문
- 공간 복잡도: `O(N × M)` — dist 3D 배열

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

using namespace std;

/*
- [백준] 2206. 벽 부수고 이동하기
- 분류: DFS_BFS
- 난이도: 골드 3
- 날짜: 2026.03.20
- 링크: https://www.acmicpc.net/problem/2206
*/
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int row, column;
vector<vector<int>> graph;
vector<vector<vector<int>>> dist;

bool inRange(int x, int y) {
    return x >= 0 && x < column && y >= 0 && y < row;
}

int bfs() {
    queue<tuple<int, int, int>> q;
    dist[0][0][0] = 1;
    q.push({0, 0, 0});

    while (!q.empty()) {
        auto [y, x, broke] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) continue;

            if (broke == 0) { // 벽을 부수지 않은 경우
                if (graph[ny][nx] == 0 && dist[ny][nx][0] == -1) { 
                    dist[ny][nx][0] = dist[y][x][0] + 1;
                    q.push({ny, nx, 0});
                } else if (graph[ny][nx] == 1 && dist[ny][nx][0] == -1) { // 그 다음 칸이 벽인 경우
                    dist[ny][nx][1] = dist[y][x][0] + 1;
                    q.push({ny, nx, 1}); 
                }
            } else { // 벽을 부순 경우
                if (graph[ny][nx] == 0 && dist[ny][nx][1] == -1) {
                    dist[ny][nx][1] = dist[y][x][1] + 1;
                    q.push({ny, nx, 1});
                }
            }
        }
    }

    int ans = -1;
    for (int i = 0; i < 2; i++) {
        if(dist[row-1][column-1][i] != -1) {
            if (ans == -1) ans = dist[row-1][column-1][i];
            else ans = min(ans, dist[row-1][column-1][i]);
        }
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> row >> column;
    graph.assign(row, vector<int>(column));
    dist.assign(row, vector<vector<int>>(column, vector<int>(2, -1))); // 벽을 부수지 않은 경우의 dist와 벽을 부수고 났을 때의 dist

    for (int i = 0; i < row; i ++) {
        string nums;
        cin >> nums;
        for (int j = 0; j < column; j++) graph[i][j] = nums[j] - '0';
    }

    cout << bfs() << "\n";

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|오답 (-1)|미방문 체크 조건 누락 및 broke 상태 오류|
|2차|오답 (14)|시작점 dist를 0으로 초기화 (1이어야 함)|
|3차|정답 (15)||

### 상세 원인

**1차 오류 — 미방문 체크 및 broke 상태 오류**

```cpp
// 잘못된 코드
} else if (dist[ny][nx][0] == -1) {   // dist[0]을 체크했지만 dist[1]에 저장
    dist[ny][nx][1] = dist[y][x][0] + 1;

// 수정된 코드
} else if (graph[ny][nx] == 1 && dist[ny][nx][1] == -1) {  // 벽인지 + dist[1] 미방문 체크
    dist[ny][nx][1] = dist[y][x][0] + 1;
```

벽 부수고 이동 후에도 큐에 push하지 않아 탐색이 중단되는 문제도 있었다.

**2차 오류 — 시작점 거리 초기화**

```cpp
// 잘못된 코드
dist[0][0][0] = 0;  // (0,0)을 거리 0으로 초기화

// 수정된 코드
dist[0][0][0] = 1;  // 문제에서 시작 칸도 1로 카운트
```

### 개선점

- 미방문 체크는 반드시 해당 상태의 dist를 체크해야 한다. `dist[ny][nx][broke]`
- 큐에 push할 때는 항상 dist 업데이트와 세트로 해야 한다
- 문제에서 거리를 칸의 개수로 셀 때는 시작점을 1로 초기화

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. 상태 BFS (State-based BFS)

일반 BFS는 `dist[y][x]`로 좌표만 상태로 관리하지만, **추가 조건이 있을 때는 차원을 늘려 상태를 함께 저장**한다.

```cpp
// 일반 BFS
dist[y][x]

// 상태 BFS — 벽 부수기 여부 추가
dist[y][x][broke]  // broke: 0(안 부숨), 1(부쉈음)
```

큐에도 상태를 함께 저장해야 꺼낼 때 현재 상태를 알 수 있다:
```cpp
queue<tuple<int, int, int>> q;
q.push({y, x, broke});
```

**이 패턴을 쓰는 조건**: "특정 행동을 제한된 횟수만 할 수 있다"는 조건이 있을 때
- 벽을 K번 부술 수 있다 → `dist[y][x][k]`
- 순간이동을 1번 쓸 수 있다 → `dist[y][x][used]`

### 2. graph vs dist 분리

최단 경로 BFS에서는 두 배열을 분리하는 것이 기본 패턴이다:

```cpp
graph[y][x]  // 맵 정보 (0: 빈칸, 1: 벽) — 읽기 전용
dist[y][x]   // 최단 거리 저장, -1은 미방문 — 쓰기용
```

`dist`를 `-1`로 초기화하면 별도의 `visited` 배열 없이 방문 여부도 겸할 수 있다.
