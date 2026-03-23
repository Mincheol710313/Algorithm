#include <bits/stdc++.h>
using namespace std;

int node_num, edge_num, start;
vector<vector<int>> graph;
vector<bool> visited;

void dfs(int cur) {
    visited[cur] = true;
    cout << cur << " ";

    for (int next : graph[cur]) {
        if (!visited[next]) {
           dfs(next);
        }
    }

}

void bfs() {
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front(); q.pop();
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
    cin >> node_num >> edge_num >> start;   
    graph.assign(node_num+1, vector<int>());
    visited.assign(node_num+1, false);

    for (int i = 0; i < edge_num; i++) {
        int node1, node2;
        cin >> node1 >> node2;
        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }

    for (int i = 0; i < node_num; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(start);
    cout << "\n";
    fill(visited.begin(), visited.end(), false);
    bfs();

    return 0;
}
