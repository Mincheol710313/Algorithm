
# [백준] 2606. 바이러스

> 🔗 [문제 링크](https://www.acmicpc.net/problem/2606) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `실버 3`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  |MB      |
|실행 시간|ms      |
|제출 일자|2026.04.03|
|사용 언어|C++     |

-----

## 📝 문제 설명

```text
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
```

### 입력
```text
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```

### 출력
```text
4
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

1번 컴퓨터에서 연결된 모든 컴퓨터를 탐색하면 되니 DFS로 접근했다. 인접 리스트로 그래프를 구성하고, 방문 여부를 `visited` 배열로 관리하면 된다고 생각했다.

### 2. 핵심 아이디어

DFS 함수에서 **현재 노드(`cur_node`)의 인접 리스트**를 순회하며 재귀 호출한다.

예시(7대, 6개 간선)에서 DFS 탐색 흐름:

```
dfs(1) → visited[1] = true
  └─ 인접: [2, 5]
     dfs(2) → visited[2] = true
       └─ 인접: [1, 3, 5]
          dfs(3) → visited[3] = true  (인접: [2] → 모두 방문됨)
     dfs(5) → visited[5] = true
       └─ 인접: [1, 2, 6]
          dfs(6) → visited[6] = true  (인접: [5] → 모두 방문됨)

결과: 2, 3, 5, 6 → 총 4대
```

노드 4, 7은 1번과 연결되지 않으므로 visited 상태가 false로 남는다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(V + E)` — 각 노드와 간선을 한 번씩 방문
- 공간 복잡도: `O(V + E)` — 인접 리스트 + visited 배열

-----

## 💻 최종 코드

```cpp
#include <bits/stdc++.h>
using namespace std;

int computer, edge;
vector<vector<int>> graph;
vector<bool> visited;

void dfs(int cur_node) {
    visited[cur_node] = true;

    for(int node : graph[cur_node]) {
        if(!visited[node]) dfs(node);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> computer;
    cin >> edge;
    graph.assign(computer+1, vector<int>(0));
    visited.assign(computer+1, false);
    
    for (int i = 0; i < edge; i++) {
        int first, second;
        cin >> first >> second;

        graph[first].push_back(second);
        graph[second].push_back(first);
    }

    dfs(1);

    int count = 0;
    for (int i = 2; i <= computer; i++) {
        if(visited[i]) count++;
    }

    cout << count;

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차|오답|DFS 함수 내에서 `cur_node` 대신 `1`을 하드코딩|

### 상세 원인

```cpp
// 잘못된 코드 — 항상 노드 1의 인접 리스트만 순회
for(int node : graph[1]) {
    if(!visited[node]) dfs(node);
}

// 올바른 코드 — 현재 탐색 중인 노드의 인접 리스트를 순회
for(int node : graph[cur_node]) {
    if(!visited[node]) dfs(node);
}
```

DFS의 핵심은 **재귀 호출 시 매개변수로 받은 현재 노드**를 기준으로 탐색하는 것이다. `graph[1]`로 고정하면 재귀가 깊어져도 항상 노드 1의 이웃만 반복 방문하고, 실제로 그래프 전체를 탐색하지 못한다.

### 개선점

- DFS 함수를 작성할 때 순회 대상이 `graph[cur_node]`인지 항상 확인한다.
- 매개변수 이름(`cur_node`)과 실제 사용하는 인덱스가 일치하는지 체크하는 습관을 들인다.

-----

## 💡 배운 점 & 다음에 써먹을 패턴

### 1. DFS 기본 구조

재귀 DFS는 항상 **현재 노드(`cur_node`)** 를 방문 처리하고, 그 노드의 인접 리스트를 순회하는 구조를 유지한다.

```cpp
void dfs(int cur_node) {
    visited[cur_node] = true;          // 현재 노드 방문 처리
    for(int node : graph[cur_node]) {  // 현재 노드의 인접 노드 순회
        if(!visited[node]) dfs(node);
    }
}
```

### 2. 연결 요소(Connected Component) 카운팅 패턴

1번 노드에서 DFS/BFS를 한 번 돌린 후, `visited` 배열에서 true인 노드를 세면 연결된 컴포넌트의 크기를 구할 수 있다.

```cpp
dfs(1);
int count = 0;
for (int i = 2; i <= n; i++) {
    if(visited[i]) count++;
}
```
