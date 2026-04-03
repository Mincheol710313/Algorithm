# [백준] 7576. 토마토(2D)

> 🔗 [문제 링크](https://www.acmicpc.net/problem/7576) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `골드 5`

---

## 📊 성능 요약

|     | 결과 |
|-----|------|
| 메모리 | MB |
| 실행 시간 | ms |
| 제출 일자 | 2026.04.03 |
| 사용 언어 | C++ |

---

## 📝 문제 설명

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

### 입력
```text
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
```

### 출력
```text
8
```

---

## 🧠 풀이 과정

### 1. 처음 접근 방법

익은 토마토가 하루마다 인접한 칸으로 퍼진다는 점에서 BFS를 떠올렸다.
단, 시작점이 여러 개일 수 있으므로 처음에 익은 토마토(1)를 **모두 큐에 넣고** BFS를 시작하는 다중 시작점 BFS로 접근했다.

### 2. 핵심 아이디어

- 처음에 `grid[i][j] == 1`인 칸을 전부 큐에 넣고 BFS 시작 (다중 시작점)
- 인접한 미방문 칸(0)으로 이동할 때 `grid[ny][nx] = grid[cy][cx] + 1`로 날짜 누적
- BFS 종료 후 grid를 순회해 0이 남아있으면 -1 반환, 아니면 최댓값 - 1 반환
- 토마토가 없는 칸(-1)은 건너뛰고, 결과는 시작값(1)이 포함되므로 최종 출력 시 -1 처리

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(N * M)` — 모든 칸을 최대 한 번 방문
- 공간 복잡도: `O(N * M)` — grid 배열 + BFS 큐

---

## 💻 최종 코드
```cpp
#include <bits/stdc++.h>
using namespace std;

/*
- [백준] 7576. 토마토(2D)
- 분류: DFS_BFS
- 난이도: 골드 5
- 날짜: 2026.04.03
- 링크: https://www.acmicpc.net/problem/7576
*/
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int y, x;
vector<vector<int>> grid;

bool inRange(int ny, int nx) {
    return ny >= 0 && ny < y && nx >= 0 && nx < x;
}

int bfs() {
    queue<tuple<int, int>> q;

    for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
            if (grid[i][j] == 1) q.push({i,j});
        }
    }

    while(!q.empty()) {
        auto [cy, cx] = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if (inRange(ny,nx) && grid[ny][nx] == 0) {
                grid[ny][nx] = grid[cy][cx] + 1;
                q.push({ny, nx});
            }
        }
    }

    int result = -1;
    for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
            if (grid[i][j] == 0) return -1;
            else if (grid[i][j] == -1) continue;
            else {
                if(result == -1) result = grid[i][j];
                else result = max(result, grid[i][j]);
            }
        }
    }
    
    return result-1;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    cin >> x >> y;
    grid.assign(y, vector<int>(x, 0));

    for (int i = 0; i < y; i++) {
        for(int j = 0; j < x; j++) {
            cin >> grid[i][j];
        }
    }

    cout << bfs();

    return 0;
}
```

---

## ❌ 틀린 이유 & 개선점

| 시도 | 결과 | 원인 |
|--|--|--|
| 1차 | 정답 | - |

---

## 💡 배운 점 & 다음에 써먹을 패턴

- **다중 시작점 BFS**: 시작 조건(익은 토마토)에 해당하는 칸을 처음에 전부 큐에 넣고 BFS 시작
- **BFS 결과값 -1**: 시작 토마토의 값(1)이 카운트에 포함되므로 최종 출력 시 `result - 1` 필요
- **불가능 케이스 처리**: BFS 후 grid에 0이 남아있으면 -1 반환
- **거리 누적 방식**: 별도 dist 배열 없이 grid 값 자체에 `grid[cy][cx] + 1`로 날짜 누적 가능
- **토마토 없는 칸(-1) 처리**: 결과 집계 시 -1인 칸은 `continue`로 건너뛰어야 함