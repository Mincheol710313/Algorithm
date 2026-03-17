
# [백준] 1260. DFS와 BFS

> 🔗 [문제 링크](https://www.acmicpc.net/problem/1260) | 📁 분류: `DFS_BFS` | ⭐ 난이도: `실버 2`

-----

## 📊 성능 요약

|     |결과      |
|-----|--------|
|메모리  | 2288 KB |
|실행 시간| 0 ms |
|제출 일자|2026.03.17|
|사용 언어|C++     |

-----

## 📝 문제 설명

> 문제에 대한 설명을 여기에 작성하세요
```text
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
```

### 입력
```text
4 5 1
1 2
1 3
1 4
2 4
3 4
```

### 출력
```text
1 2 4 3
1 2 3 4
```

-----

## 🧠 풀이 과정

### 1. 처음 접근 방법

> 문제를 보고 처음에 어떻게 생각했는지 서술 (틀린 접근도 OK)

문제 자체가 DFS와 BFS 알고리즘을 구현할 수 있는지 물어보는 문제이기 때문에 각 알고리즘을 구현해서 풀려고 했다.

### 2. 핵심 아이디어

> 문제를 푸는 핵심 발상이 무엇인지

DFS와 BFS 알고리즘을 함수를 구현하여서 문제를 풀었다. 하지만 중요한 부분이 **방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문**이여서 정렬한 후에 DFS와 BFS 알고리즘을 적용했다.

### 3. 시간/공간 복잡도 분석

- 시간 복잡도: `O(MlogM)` - `graph`의 각 배열에 대해서 정렬 전처리를 하는 과정이 시간 복잡도가 `O(NlogN)`으로 가장 크다. 또한 DFS와 BFS 알고리즘은 `O(N+M)`의 시간복잡도를 가진다. 
- 공간 복잡도: `O(N²)` - 최악의 경우, 완전 그래프로 `O(N²)`의 공간복잡도를 가진다.

-----

## 💻 최종 코드

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

/*
- [백준] 1260. DFS와 BFS
- 분류: DFS_BFS
- 난이도: 실버 2
- 날짜: 2026.03.17
- 링크: https://www.acmicpc.net/problem/1260
*/
void dfs(vector<vector<int>>& graph, int start, vector<bool>& visited) {
    visited[start] = true;
    cout << start << " ";

    for (int node : graph[start]) {
        if (!visited[node]) {
            dfs(graph, node, visited);
        }
    }
}

void bfs(vector<vector<int>>& graph, int start, vector<bool>& visited) {
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int i : graph[node]) {
            if (!visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
// TODO: 풀이 작성
    int node_num, line_num, start_node;
    cin >> node_num >> line_num >> start_node;

    vector<vector<int>> graph;
    vector<bool> visited(node_num+1, false);
    for (int i = 0; i < node_num + 1; i++) {
        graph.push_back({});
    }

    for (int i = 0; i < line_num; i++) {
        int node, conect_node;
        cin >> node >> conect_node;
        graph[node].push_back(conect_node);
        graph[conect_node].push_back(node);
    }
    
    for(int i = 1; i < node_num + 1; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(graph, start_node, visited);
    cout << "\n";
    fill(visited.begin(), visited.end(), false);
    bfs(graph, start_node, visited);
    cout << "\n";

    return 0;
}
```

-----

## ❌ 틀린 이유 & 개선점

|시도|결과|원인|
|--|--|--|
|1차| Sucess|  |

-----

## 💡 배운 점 & 다음에 써먹을 패턴

- `vector`는 `memset`으로 초기화하면 안 된다.
  - `vector`는 데이터가 힙에 있고, 객체 자체는 포인터/크기/용량 정보만 담고 있다.
  - `memset(&visited, false, sizeof(visited))`는 포인터 정보를 덮어써서 **UB(Undefined Behavior)** 또는 크래시를 유발한다.
  - **올바른 초기화 패턴:**
    ```cpp
    // 방법 1: fill (권장)
    fill(visited.begin(), visited.end(), false);

    // 방법 2: assign
    visited.assign(visited.size(), false);
    ```
  - `memset`은 `int arr[]`, `bool arr[]` 같은 **C 스타일 배열**에만 안전하게 쓸 수 있다.
