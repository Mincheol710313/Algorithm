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
